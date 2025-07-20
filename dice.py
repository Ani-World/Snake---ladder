from tkinter import *
import random
import time

class Die:
    def __init__(self, parent, callback=None):
        self.callback = callback
        self.frame = Frame(parent)

        self.dice_images = [
            PhotoImage(file="images/die1.png"),
            PhotoImage(file="images/die2.png"),
            PhotoImage(file="images/die3.png"),
            PhotoImage(file="images/die4.png"),
            PhotoImage(file="images/die5.png"),
            PhotoImage(file="images/die6.png"),
        ]

        self.label = Label(self.frame, text="Roll the Die", font=("Arial", 14))
        self.label.pack(pady=10)

        self.image_label = Label(self.frame, image=self.dice_images[0])
        self.image_label.pack(pady=10)

        # self.button = Button(self.frame, text="Roll", font=("Arial", 14), command=self.roll_die)
        # self.button.pack(pady=10)

        self.frame.grid(row=0, column=1, padx=20)

    def roll_die(self):
        # Animate rolling
        for _ in range(10):
            temp_img = random.choice(self.dice_images)
            self.image_label.config(image=temp_img)
            self.image_label.update()
            time.sleep(0.05)

        result = random.randint(1, 6)
        self.image_label.config(image=self.dice_images[result - 1])

        if self.callback:
            self.callback(result)
