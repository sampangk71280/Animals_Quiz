# Hard GUI (component 5) for Animals Quiz

from tkinter import *
from functools import partial # to prevent unwanted windows
import random
import csv
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
                                       #command= self.to_easy,
                                  font=button_font, bg=easy_bg, width=7)
        self.easy_button.grid(row=0, column=0, padx=25, pady=15)
        self.easy_button.config(state=DISABLED)

        # Hard button
        self.hard_button = Button(self.button_frame, text="Hard",
                                  command=self.to_hard,
                                  font=button_font, bg=hard_bg, width=7)
        self.hard_button.grid(row=0, column=1, padx=25, pady=15)
        self.hard_button.config(state=DISABLED)

        # Help Button
        self.help_button = Button(self.start_frame, text="Help/Rules",
                                  bg="#badaaa", font=button_font, width=25)
        self.help_button.grid(row=5, pady=10)


    # integer checker
    # reused from mystery box and edited to suit animal quiz
    def int_check(self):
        self.starting_balance = self.question_entry.get()

        # Disable all difficulty buttons until the user has confirmed the amount of questions
        self.easy_button.config(state=DISABLED)
        self.hard_button.config(state=DISABLED)

        # Set error background colours and assume that there are no
        # errors at the start...
        error_back = "e2d6ff" # same as background_colour
        has_errors = "yes"

        try:
            self.starting_balance = int(self.starting_balance)

            # less than 0 questions, breaks
            if self.starting_balance <= 0:
                error_feedback = "Sorry you must enter a number higher than 0!"
            # more than 20 questions, breaks
            elif self.starting_balance > 20:
                error_feedback = "Too high! The maximum questions " \
                                 "you can answer is 20"
            # 1-20 questions, works
            else:
                self.easy_button.config(state=NORMAL)
                self.hard_button.config(state=NORMAL)
                error_feedback = "" # removes previous error message

        except ValueError:
            error_feedback = "Please enter an integer (no text / decimals)"

        if has_errors == "yes":
            self.question_error_label.config(text=error_feedback) # shows error message
        else:
            # set question to amount entered by user
            self.starting_questions.get(self.starting_balance)
        print(self.starting_balance)


    def to_hard(self):
        # retrieve starting balance
        self.starting_balance = self.starting_questions.get()

        Hard(self)

        # hide start up window
        self.start_frame.destroy()


class Hard:
    def __init__(self, partner):



        # colours and fonts
        background_colour = "#e2d6ff" # purple
        button_font = "Arial 12 bold"
        next_bg = "light gray"
        skip_bg= "#f29f9f" # light red
        stats_bg ="#fbac47" # orange

        # set question number and grade to 0 at the beginning
        self.question_num = 0
        self.grade = 0
        self.max_num = IntVar()
        self.max_num.set(self.starting_balance) # sets the maximum of questions asked
        print(self.max_num)

        # GUI To get starting balance and stakes
        self.hard_frame = Frame(padx=10, pady=10, bg=background_colour)
        self.hard_frame.grid()

        # Question heading (row 0)
        self.question_num_label = Label(self.hard_frame, font="Arial 19 bold", justify=LEFT, bg=background_colour)
        self.question_num_label.grid(row=0)

        # Question (row 1)
        self.ask_question = Label(self.hard_frame, wrap=350, justify=LEFT, padx=10, pady=10, bg=background_colour)
        self.ask_question.grid(row=1)

        # Entry box ... (row 2)
        # Entry Frame
        self.entry_frame = Frame(self.hard_frame, bg=background_colour)
        self.entry_frame.grid(row=2, pady=10)

        # Answer Entry Box
        self.answer_entry = Entry(self.entry_frame, font="Arial 16 bold")
        self.answer_entry.lower()
        self.answer_entry.grid(row=0, column=0)

        # Answer Confirm button
        self.confirm_button = Button(self.entry_frame, font=button_font,
                                     text="OK", bg=next_bg, command=self.check_answer)

        # binding not working
        self.confirm_button.focus()
        self.confirm_button.bind('<Return>', lambda e: self.check_answer())

        self.confirm_button.grid(row=0, column=1)

        # User Feedback
        self.feedback = Label(self.hard_frame, font="Arial 12", bg=background_colour) # some reason it's not working
        self.feedback.grid(row=3)

        # Button frame (row 3)
        self.button_frame = Frame(self.hard_frame, bg=background_colour)
        self.button_frame.grid(row=4)

        # Skip Button
        self.skip_button = Button(self.button_frame, font=button_font,
                                  text="Skip", bg=skip_bg, command=lambda:self.generate_ques())
        self.skip_button.grid(row=0, column=0, padx=5, pady=10)

        # Next Button
        self.next_button = Button(self.button_frame, font=button_font,
                                  text="Next", bg=next_bg, command=lambda:self.generate_ques())
        self.next_button.grid(row=0, column=1, padx=5, pady=10)

        # label for first tion
        self.first = Label(self.button_frame, command=self.generate_ques())

        # Quiz Statistics Button (row 5)
        self.stats_button = Button(self.hard_frame, text="Quiz Statistics",
                                  bg=stats_bg, font=button_font, width=25,
                                    ) #,command=self.help)
        self.stats_button.grid(row=5, pady=10)

    def generate_ques(self):
        results = [] # contains the adult and baby term
        with open('animals_quiz(final).csv') as file:
            # make csv file into a list
            reader = csv.reader(file)
            next(reader) # skips the heading in csv
            for row in reader:
                results.append(row)

        question_list = random.choice(results)  # randomly chooses a row


        question = question_list[0]  # adult animal term
        self.answer = question_list[1]  # baby animal term

        print(question, self.answer)
        # asks questions
        self.ask = ("What is the baby term for {}?".format(question))
        self.ask_question.config(text=self.ask)

        # adds one to the question number
        self.question_num += 1
        self.question_num_label.config(text="Question {}/{}".format(self.question_num, self.max_num))

        self.confirm_button.config(state=NORMAL) # enables for the next question
        self.next_button.config(state=DISABLED)  # enables for the next question

    def check_answer(self):
        # different praises
        praise_list = ["Good job!", "Well done!", "Amazing!", "You did well!"]


        # takes the answer
        self.user_answer = self.answer_entry.get()
        self.user_answer = self.user_answer.lower() # turns entry to lowercase

        self.next_button.config(state=NORMAL)
        # if answer is correct
        if self.user_answer == self.answer:
            self.grade += 1 # add a point to grade
            praise = random.choice(praise_list) # randomly picked praises
            self.user_feedback = praise
            # disables confirm button so the user only gets one guess
            self.confirm_button.config(state=DISABLED) # disables while checking so user can't change it
            self.next_button.config(state=NORMAL) # user can only go to the next question if they have answered

        # if answer is blank
        elif self.user_answer == "":
            self.user_feedback = ("Please don't leave it blank!")
            # button does not get disabled here
            self.next_button.config(state=DISABLED)  # keep next button disabled

        # incorrect answer
        else:
            self.user_feedback = ("Incorrect!")
            self.confirm_button.config(state=DISABLED)  # disables confirm button so the user only gets one guess
            self.next_button.config(state=NORMAL) # user can only go to the next question if they have answered

        # sets the feedback
        self.feedback.config(text=self.user_feedback)
        print(self.grade)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Animals Quiz")
    something = Start(root)
    root.mainloop()
