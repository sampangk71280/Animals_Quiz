# Help GUI (component 2) for Animals Quiz

from tkinter import *
from functools import partial # to prevent unwanted windows
import random


class Hard:
    def __init__(self, parent):

        # colours and fonts
        background_colour = "#e2d6ff" # purple
        button_font = "Arial 12"
        next_bg = "light gray"
        skip_bg= "#f29f9f" # light red
        stats_bg ="#fbac47" # orange

        # text
        question_num = 1 # for testing purpose, change in the future
        ask = "What is the baby term for a cow?"

        # GUI To get starting balance and stakes
        self.hard_frame = Frame(padx=10, pady=10, bg=background_colour)
        self.hard_frame.grid()

        # Animal Heading (row 0)
        self.question_num_label = Label(self.hard_frame, text="Question {}/20".format(question_num),
                                       font="Arial 19 bold", justify=LEFT, bg=background_colour)
        self.question_num_label.grid(row=0)

        # Instructions (row 1)
        self.ask_question = Label(self.hard_frame, text="Question: {}".format(ask),
                                         wrap=350, justify=LEFT, padx=10, pady=10, bg=background_colour)
        self.ask_question.grid(row=1)

        # Entry box ... (row 2)
        # Entry Frame
        self.entry_frame = Frame(self.hard_frame, bg=background_colour)
        self.entry_frame.grid(row=2, pady=10)

        # Answer Box
        self.answer_entry = Entry(self.entry_frame, font="Arial 16 bold")
        self.answer_entry.grid(row=0, column=0)

        # skip row for aesthetic purposes
        # Button frame (row 3)
        self.button_frame = Frame(self.hard_frame, bg=background_colour)
        self.button_frame.grid(row=3)

        # Skip Button
        self.skip_button = Button(self.button_frame, font="Arial 12 bold",
                                  text="Skip", bg=skip_bg)  # ,command=self. , font=, width)
        self.skip_button.grid(row=0, column=0, padx=5, pady=10)

        # Next Button
        self.next_button = Button(self.button_frame, font="Arial 12 bold",
                                  text="Next", bg=next_bg)  # , command=self., font=, width)
        self.next_button.grid(row=0, column=1, padx=5, pady=10)

        # Quiz Statistics Button
        self.stats_button = Button(self.hard_frame, text="Quiz Statistics",
                                  bg=stats_bg, font=button_font, width=25,
                                    ) #,command=self.help)
        self.stats_button.grid(row=4, pady=10)






# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Animals Quiz")
    something = Hard(root)
    root.mainloop()
