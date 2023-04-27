from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("french_words.csv")
new_dict = data.to_dict(orient="records")
new_random = {}

def random_word():
    global new_random
    new_random = random.choice(new_dict)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=new_random["French"])

def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=new_random["English"])

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, func=flip_card)

canvas = Canvas(window, height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
image_front = PhotoImage(file="card_front.png")
image_back = PhotoImage(file="card_back.png")
canvas_image = canvas.create_image(400, 263, image=image_front)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=('Ariel 40 italic'))
card_word = canvas.create_text(400, 263, text="", font=('Ariel 60 bold'))

image_left = PhotoImage(file="wrong.png")
button_left = Button(image=image_left, highlightthickness=0, command=random_word)
button_left.grid(row=1, column=0)

image_right = PhotoImage(file="right.png")
button_right = Button(image=image_right, highlightthickness=0, command=random_word)
button_right.grid(row=1, column=1)

random_word()



window.mainloop()