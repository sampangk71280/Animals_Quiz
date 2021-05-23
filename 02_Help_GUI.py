# Help GUI (component 2) for Animals Quiz

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
        self.entry_error_frame = Frame(self.start_frame, bg=background_colour)
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
                                  font=button_font, bg=easy_bg, width=7)
        self.easy_button.grid(row=0, column=0, padx=25, pady=15)
        self.easy_button.config(state=DISABLED)

        # Hard button
        self.hard_button = Button(self.button_frame, text="Hard",
                                  command=lambda: self.to_game(2),
                                  font=button_font, bg=hard_bg, width=7)
        self.hard_button.grid(row=0, column=1, padx=25, pady=15)
        self.hard_button.config(state=DISABLED)

        # Help Button
        self.help_button = Button(self.start_frame, text="Help/Rules",
                                  bg="#badaaa", font=button_font, width=25,
                                  command=self.help)
        self.help_button.grid(row=5, pady=10)


    # integer checker
    # reused from mystery box and edited to suit animal question
    def int_check(self):
        starting_balance = self.question_entry.get()

        # Disable all difficulty buttons until the user has confirmed the amount of questions
        self.easy_button.config(state=DISABLED)
        self.hard_button.config(state=DISABLED)

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

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="This animal quiz will test your knowledge "
                                          "on baby terms for different animals. "
                                          "There are up to 20 questions you may "
                                          "choose to answer, with all the animals "
                                          "chosen at random. \n\n"
                                          "In Hard mode, there is an option to receive "
                                          "a hint for each question or to skip. "
                                          "In Easy mode there are no hints or skip available. \n\n"
                                          "When you are finished, you can view your Game Statistics "
                                          "which can be saved and exported into a text file.",
                                     padx=10)
# copied from mystery boxes
class Help:
    def __init__(self, partner):

        background_colour = "#b8daaa" # light green back ground colour

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background_colour)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Rules",
                                 font="arial 10 bold", bg=background_colour)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, wrap=250, bg=background_colour)
        self.help_text.grid(column=0, row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="#f29f9f",
                                  font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Animals Quiz")
    something = Start(root)
    root.mainloop()
