# Component 1 - Start GUI

from tkinter import *
from functools import partial # to prevent unwanted windows
import random

class Start:
    def __int__(self, partner):

        background_colour = "#e2d6ff" # purple

        # Start Frame
        self.start_frame = Frame(padx=10, pady=10, bg=background_colour)
        self.start_frame.grid()

        # Animal Heading (row 0)
        self.animal_quiz_label = Label(self.start_frame, text="Animal Quiz",
                                       font="Arial 19 bold", bg=background_colour)
        self.animal_quiz_label.grid(row=0)

        # Welcome text (row 1)
        self.animal_welcome = Label(self.start_frame, font="Arial 10",
                                    text="Welcome to the Animal Quiz! "
                                         "Choose whether you want to play hard to easy mode! "
                                         "Easy mode is multi-choice and in Hard mode you have "
                                         "to enter the full answers yourself. "
                                         "It is suggested to read the help/rules if "
                                         "this is your first time.",
                                    wrap=275, justify=LEFT, padx=10, pady=10, bg=background_colour)

        # How many questions
        self.questions_amount = Label(self.start_frame, font="Arial 12 bold",
                                      text="How many questions do you want to "
                                           "be tested on?",
                                      wrap=275, justify=CENTER, padx=10, pady=10, bg=background_colour)

        # Entry box


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Animals Quiz")
    something = Start()
    root.mainloop()
