# Start GUI (component 1) for Animals Quiz

from tkinter import *
from functools import partial # to prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # colours and fonts
        background_colour = "#e2d6ff" # purple
        button_font = "Arial 16 bold"
        easy_bg = "#ffc1dc"  # light pink
        hard_bg = "#cadcfb" # light blue

        # GUI To get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10, bg=background_colour)
        self.start_frame.grid()

        # Set initial questions to zero
        self.starting_questions = IntVar()
        self.starting_questions.set(0)

        # Animal Heading (row 0)
        self.animal_quiz_label = Label(self.start_frame, text="Animals Quiz",
                                       font="Arial 19 bold", bg=background_colour)
        self.animal_quiz_label.grid(row=0)

        # Instructions (row 1)
        self.animal_instructions = Label(self.start_frame, text="Welcome to the Animal Quiz! Choose "
                                                                "whether you want to play hard to easy "
                                                                "mode! Easy mode is multi-choice and in "
                                                                "Hard mode you have to enter the full answers "
                                                                "yourself. It is suggested to read the help/rules "
                                                                "if this is your first time.",
                                         wrap=350, justify=LEFT, padx=10, pady=10, bg=background_colour)
        self.animal_instructions.grid(row=1)

        # How many question (row 2)
        self.how_many=Label(self.start_frame, text="How many questions do you want to answer?",
                            wrap=300, padx=10, pady=10, bg=background_colour, font="Arial 10 bold")
        self.how_many.grid(row=2)

        # Entry box ... (row 3)
        # Entry Frame
        self.entry_error_frame = Frame(self.start_frame, width=200, bg=background_colour)
        self.entry_error_frame.grid(row=3)

        # Entry box
        self.question_entry = Entry(self.entry_error_frame, font="Arial 16 bold")
        self.question_entry.grid(row=0, column=0)

        # Question button
        self.confirm_button = Button(self.entry_error_frame, font="Arian 12 bold",
                                     text="Confirm",command=self.int_check)
        self.confirm_button.grid(row=0, column=1, padx=5)

        # Error message
        self.question_error_label=Label(self.entry_error_frame, fg="maroon",
                                        text="", font="Arial 10 bold",
                                        wrap=275, justify=LEFT, bg=background_colour)
        self.question_error_label.grid(row=1, columnspan=2, pady=5)


        # Button frame (row 4)
        self.button_frame = Frame(self.start_frame, bg=background_colour)
        self.button_frame.grid(row=4)

        # Difficulty Buttons
        # Easy button
        self.easy_button = Button(self.button_frame, text="Easy",
                                       command=lambda: self.to_game(1),
                                  font=button_font, bg=easy_bg)
        self.easy_button.grid(row=0, column=0, padx=25, pady=10)

        # Hard button
        self.hard_button = Button(self.button_frame, text="Hard",
                                  command=lambda: self.to_game(2),
                                  font=button_font, bg=hard_bg)
        self.hard_button.grid(row=0, column=1, padx=25, pady=10)

        # Help Button
        self.help_button = Button(self.start_frame, text="Help/Rules",
                                  bg="#badaaa", font=button_font)
        self.help_button.grid(row=5, pady=10)

        # Disable all difficulty buttons until the user has confirmed the amount of questions
        self.easy_button.config(state=DISABLED)
        self.hard_button.config(state=DISABLED)

    # integer checker
    # reused from mystery box and edited to suit animal question
    def int_check(self):
        starting_balance = self.question_entry.get()

        # Set error background colours and assume that there are no
        # errors at the start...
        error_back = "e2d6ff" # same as background_colour
        has_errors = "no"

        try:
            starting_balance = int(starting_balance)

            # less than 0 questions, breaks
            if starting_balance < 0:
                has_errors = "yes"
                error_feedback = "Sorry you must enter a number higher than 0!"
            # more than 20 questions, breaks
            elif starting_balance > 20:
                has_errors = "yes"
                error_feedback = "Too high! The maximum questions " \
                                 "you can answer is 20"
            # 1-20 questions, works
            else:
                self.easy_button.config(state=NORMAL)
                self.hard_button.config(state=NORMAL)

        except ValueError:
            has_errors = "yes"
            error_feedback = "Pllease enter an integer (no text / decimals)"

        if has_errors == "yes":
            self.question_error_label.config(text=error_feedback)
        else:
            # set starting balance to amount entered by user
            self.starting_questions.set(starting_balance)



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Animals Quiz")
    something = Start(root)
    root.mainloop()
