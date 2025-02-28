import tkinter as tk
import random

# Thai consonants and their names (just a sample, you can add more).
consonants = [
    ("ก", "gor kai"),
    ("ข", "khor khai"),
    ("ค", "khor khuat"),
    ("ง", "ngor ngu"),
    ("จ", "jor jan"),
    ("ฉ", "chor ching"),
    ("ช", "chor chang"),
    ("ซ", "sor so"),
    ("ฌ", "chor chao"),
    ("ญ", "yor ying")
]

class FlashcardGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Thai Consonant Flashcards")
        self.geometry("400x300")

        # Initial setup for the flashcard.
        self.current_card = None
        self.is_flipped = False

        self.card_label = tk.Label(self, text="", font=("Helvetica", 48), width=10, height=5)
        self.card_label.pack(pady=50)

        self.flip_button = tk.Button(self, text="Flip", command=self.flip_card)
        self.flip_button.pack(pady=20)

        self.next_card()

    def next_card(self):
        """Select a random consonant and display it."""
        self.current_card = random.choice(consonants)
        self.is_flipped = False
        self.card_label.config(text=self.current_card[0])  # Show consonant.

    def flip_card(self):
        """Flip the card to show its name."""
        if self.is_flipped:
            self.next_card()  # Go to the next card after flip.
        else:
            self.card_label.config(text=self.current_card[1])  # Show consonant name.
            self.is_flipped = True

if __name__ == "__main__":
    game = FlashcardGame()
    game.mainloop()
