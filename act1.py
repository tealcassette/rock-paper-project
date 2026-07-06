import random
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("game")
window.geometry("400x300")

container = Frame(window)

play = Frame(container, bg="blue")
result = Frame(container, bg="purple")

play.grid(row = 0, column = 0)

play.grid_columnconfigure(0, weight=1)
play.grid_columnconfigure(1, weight=1)
play.grid_columnconfigure(2, weight=1)

def input(choice):
    global user_input
    user_input = choice
    play.grid_remove()
    result.grid(row = 0, column = 0)

button_width = 5
button_height = 2
button_font = ("Arial", 18)

rock_button = Button(play, text="Rock", width = button_width, height = button_height, font = button_font, command = lambda: input("rock"))
paper_button = Button(play, text="Paper", width = button_width, height = button_height, font = button_font, command = lambda: input("paper"))
scissor_button = Button(play, text="Scissor", width = button_width, height = button_height, font = button_font, command = lambda: input("scissor"))

rock_button.grid(row = 2, column = 0, padx = 4, pady = 2)
paper_button.grid(row = 2, column = 1, padx = 4, pady = 2)
scissor_button.grid(row = 2, column = 2, padx = 4, pady = 2)

text = Label(play, text="Welcome to Rock-Paper-Scissor! Choose one of the options.")
text.grid(row = 0, column = 1, padx = 2, pady = 4)

rock_image = ImageTk.PhotoImage(Image.open("rock.jpg").resize((80, 80)))
paper_image = ImageTk.PhotoImage(Image.open("paper.jpg").resize((80, 80)))
scissor_image = ImageTk.PhotoImage(Image.open("scissor.jpg").resize((80, 80)))

rock_label = Label(play, image = rock_image)
paper_label = Label(play, image = paper_image)
scissor_label = Label(play, image = scissor_image)

rock_label.grid(row = 1, column = 0)
paper_label.grid(row = 1, column = 1)
scissor_label.grid(row = 1, column = 2)

def deciding_who_wins():
    global computer_input, user_input, who_wins
    
    computer_input = random.choice(["rock", "paper", "scissor"])

    if user_input == computer_input:
        who_wins = "No one wins! It's a draw."
    if user_input == "rock":
        if computer_input == "paper":
            who_wins = "The computer wins! You lose."
        if computer_input == "scissor":
            who_wins = "You win! Yay!"
    if user_input == "paper":
        if computer_input == "rock":
            who_wins = "You win! Yay!"
        if computer_input == "scissor":
            who_wins = "The computer wins! You lose."
    if user_input == "scissor":
        if computer_input == "rock":
            who_wins = "The computer wins! You lose."
        if computer_input == "paper":
            who_wins = "You win! Yay!"

computer_image = ImageTk.PhotoImage(Image.open("computer.jpg").resize((80, 80)))
draw_image = ImageTk.PhotoImage(Image.open("draw.jpg").resize((80, 80)))
you_image = ImageTk.PhotoImage(Image.open("you.jpg").resize((80, 80)))
blank_image = ImageTk.PhotoImage(Image.open("blank.jpg").resize((80, 80)))

def image_choice():
    global image
    if who_wins == "You win! Yay!":
        image = you_image
    if who_wins == "The computer wins! You lose.":
        image = computer_image
    if who_wins == "No one wins! It's a draw.":
        image = draw_image

deciding_who_wins()
image_choice()

who_wins_label = Label(result, text = who_wins)
text.grid(row = 1, column = 1, padx = 2, pady = 4)

image_label = Label(result, image = image)
image_label.grid(row = 1, column = 0)

def reset():
    result.grid_remove()
    play.grid()
    user_input = ""
    computer_input = ""
    image = blank_image
    who_wins = ""

reset_button = Button(play, text="Play Again", width = button_width, height = button_height, font = button_font, command = lambda: reset())
reset_button.grid(row = 2, column = 1, padx = 4, pady = 2)

window.mainloop()