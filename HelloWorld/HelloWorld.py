import tkinter as tk
from tkinter import messagebox
from datetime import datetime

MOODS = {
    "Happy": {"emoji": "😊", "quran": "Praise be to Allah who makes me happy. (Surah Al-Furqan 25:70)"},
    "Sad": {"emoji": "😢", "quran": "Indeed, with hardship comes ease. (Ash-Sharh 94:6)"},
    "Stressed": {"emoji": "😣", "quran": "Believe in Allah and be patient. (Al-Imran 3:200)"},
    "Tired": {"emoji": "😴", "quran": "If you are tired, rest is necessary. (Sahih Hadith)"},
    "Neutral": {"emoji": "😐", "quran": "Every day is a gift from Allah. (Surah Al-Baqarah 2:286)"},
    "Content": {"emoji": "😌", "quran": "The soul finds peace with God. (Surah Al-Fajr 89:27-28)"},
    "Trusting": {"emoji": "🙏", "quran": "Remember Allah and He will remember you. (Al-Baqarah 2:152)"},
    "Hopeful": {"emoji": "🌟", "quran": "Do not lose hope in Allah's mercy. (Az-Zumar 39:53)"},
    "Calm": {"emoji": "🕊️", "quran": "Peace for those who believe and do good deeds. (Al-Furqan 25:63)"},
    "Angry": {"emoji": "😠", "quran": "Be patient and forgive. (Al-Imran 3:134)"}
}


class MoodApp:
    def __init__(self, root):
        self.root = root
        root.title("Mood and Quranic Verse with Save & Search")
        root.geometry("600x550")
        root.resizable(False, False)

        # List to save mood history (date, mood, reason)
        self.history = []

        # Label
        tk.Label(root, text="Select your mood from the list:").pack(pady=5)

        # Listbox for moods
        self.listbox = tk.Listbox(root, height=10)
        for mood in MOODS.keys():
            self.listbox.insert(tk.END, mood)
        self.listbox.pack(padx=20, fill=tk.X)

        # Entry for reason
        tk.Label(root, text="Write the reason for your mood:").pack(pady=5)
        self.entry_reason = tk.Text(root, height=4, width=50)
        self.entry_reason.pack(padx=20)

        # Button to save mood
        tk.Button(root, text="Save Mood and Reason",
                  command=self.save_mood).pack(pady=10)

        # Text box to display result (emoji + Quran verse)
        self.text_result = tk.Text(
            root, height=6, width=65, state="disabled", wrap="word")
        self.text_result.pack(pady=10)

        # Search by date
        tk.Label(
            root, text="Search history by date (YYYY-MM-DD):").pack(pady=5)
        self.entry_search = tk.Entry(root, width=20)
        self.entry_search.pack()
        tk.Button(root, text="Search",
                  command=self.search_history).pack(pady=5)

        # Show search results
        self.text_history = tk.Text(
            root, height=10, width=65, state="disabled", wrap="word")
        self.text_history.pack(pady=10)

    def save_mood(self):
        try:
            idx = self.listbox.curselection()[0]
        except IndexError:
            messagebox.showerror(
                "Error", "Please select a mood from the list!")
            return
        mood = list(MOODS.keys())[idx]
        reason = self.entry_reason.get("1.0", tk.END).strip()
        if not reason:
            messagebox.showerror(
                "Error", "Please write the reason for your mood!")
            return
        today_date = datetime.now().strftime("%Y-%m-%d")
        # Save in history
        self.history.append({
            "date": today_date,
            "mood": mood,
            "emoji": MOODS[mood]["emoji"],
            "reason": reason,
            "quran": MOODS[mood]["quran"]
        })

        # Show emoji and Quranic verse
        self.text_result.config(state="normal")
        self.text_result.delete("1.0", tk.END)
        self.text_result.insert(tk.END,
                                f"Your mood: {mood} {MOODS[mood]['emoji']}\n\nQuranic Verse:\n{MOODS[mood]['quran']}")
        self.text_result.config(state="disabled")

        # Clear reason field
        self.entry_reason.delete("1.0", tk.END)

        messagebox.showinfo(
            "Saved", f"Mood and reason saved for date {today_date}")

    def search_history(self):
        search_date = self.entry_search.get().strip()
        if not search_date:
            messagebox.showerror("Error", "Please enter a date to search!")
            return
        # Filter history by date
        found = [h for h in self.history if h["date"] == search_date]
        self.text_history.config(state="normal")
        self.text_history.delete("1.0", tk.END)
        if not found:
            self.text_history.insert(
                tk.END, f"No records found for date {search_date}.")
        else:
            for r in found:
                self.text_history.insert(tk.END,
                                         f"Date: {r['date']}\nMood: {r['mood']} {r['emoji']}\nReason: {r['reason']}\nQuranic Verse:\n{r['quran']}\n\n")
        self.text_history.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = MoodApp(root)
    root.mainloop()
