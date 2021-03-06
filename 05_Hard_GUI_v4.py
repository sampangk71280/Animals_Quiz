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

        self.question_entry.focus()
        self.question_entry.bind('<Return>', lambda e: self.int_check())

        # Question button
        self.confirm_button = Button(self.entry_error_frame, font="Arial 12 bold",
                                     text="Confirm",command=self.int_check)
        self.confirm_button.focus()
        self.confirm_button.bind('<Return>', lambda e:self.int_check())
        self.confirm_button.grid(row=0, column=1, padx=5)

        # Error message
        self.question_error_label=Label(self.entry_error_frame, fg="maroon",
                                        text="", font="Arial 10 bold",
                                        wrap=275, justify=LEFT, bg=background_colour)
        self.question_error_label.grid(row=1, columnspan=2, pady=5)

        # Button frame (row 4)
        self.button_frame = Frame(self.start_frame, bg=background_colour)
        self.button_frame.grid(row=4)

        # Difficulty Button
        # Hard button
        self.hard_button = Button(self.button_frame, text="Start", # renamed to start after easy mode removed
                                  command=self.to_hard,
                                  font=button_font, bg=hard_bg, width=7)
        self.hard_button.grid(row=0, column=1, padx=25, pady=15)
        self.hard_button.config(state=DISABLED)

        # Help Button
        self.help_button = Button(self.start_frame, text="Help/Rules",
                                  bg="#badaaa", font=button_font, width=25,
                                  command=self.help)
        self.help_button.grid(row=5, pady=10)

    # integer checker
    # reused from mystery box and edited to suit animal quiz
    def int_check(self):
        self.starting_balance = self.question_entry.get()

        # Disable all difficulty buttons until the user has confirmed the amount of questions
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
                self.hard_button.config(state=NORMAL)
                error_feedback = "" # removes previous error message
                # allows user to hit enter key to start
                self.hard_button.focus()
                self.hard_button.bind('<Return>', lambda e: self.to_hard())

        except ValueError:
            error_feedback = "Please enter an integer (no text / decimals)"

        if has_errors == "yes":
            self.question_error_label.config(text=error_feedback) # shows error message

        print(self.starting_balance)

    def help(self):
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


    def to_hard(self):
        # retrieve starting balance
        starting_balance = self.starting_balance

        Hard(self, starting_balance)

        # hide start up window
        self.start_frame.destroy()


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


class Hard:
    def __init__(self, partner, starting_balance):

        self.results = []  # contains the adult and baby term
        # opens csv file
        with open('animals_quiz(final).csv') as file:
            # make csv file into a list
            reader = csv.reader(file)
            next(reader)  # skips the heading in csv
            for row in reader:
                self.results.append(row)

        # colours and fonts
        background_colour = "#e2d6ff" # purple
        button_font = "Arial 12 bold"
        next_bg = "light gray"
        skip_bg= "#f29f9f" # light red
        stats_bg ="#fbac47" # orange

        # set question number and grade to 0 at the beginning
        self.question_num = 0
        self.grade = 0
        self.max_num = (starting_balance) # sets the maximum of questions asked

        # Main Frame
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
        # Binds enter key to command button
        self.answer_entry.focus()
        self.answer_entry.bind('<Return>', lambda e: self.check_answer())
        self.answer_entry.grid(row=0, column=0)

        # Answer Confirm button
        self.confirm_button = Button(self.entry_frame, font=button_font,
                                     text="OK", bg=next_bg, command=self.check_answer)
        self.confirm_button.grid(row=0, column=1)


        # User Feedback (row 3)
        self.feedback = Label(self.hard_frame, font="Arial 12", bg=background_colour) # some reason it's not working
        self.feedback.grid(row=3)

        # Button frame (row 4)
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

        # First Question Label
        # automatically generates the first question
        self.first = Label(self.button_frame, command=self.generate_ques())

        # Quiz Statistics Button (row 5)
        self.stats_button = Button(self.hard_frame, text="Quiz Statistics",
                                  bg=stats_bg, font=button_font, width=25,
                                    ) #,command=self.help)
        self.stats_button.grid(row=5, pady=10)

    # generates question every time the next/skip button is clicked
    def generate_ques(self):

        question_list = random.choice(self.results)  # randomly chooses a row

        question = question_list[0]  # adult animal term
        self.answer = question_list[1]  # baby animal term

        print(question, self.answer)  # prints out answers for testing purposes

        # formats the question to the text
        self.ask = ("What is the baby term for {}?".format(question))
        self.ask_question.config(text=self.ask)

        self.results.remove(question_list) # removes the animal from list so no repeats

        # binds enter key to OK button
        self.confirm_button.focus()
        self.confirm_button.bind('<Return>', lambda e:self.check_answer())

        # adds one to the question number
        self.question_num += 1
        self.question_num_label.config(text="Question {}/{}".format(self.question_num, self.max_num))

        # enabled to check answer
        self.confirm_button.config(state=NORMAL)
        # disabled when user has not guessed, user needs to skip for next question without guessing
        self.next_button.config(state=DISABLED)

        # clears the entry box after each question
        self.answer_entry.delete(0, END)
        self.answer_entry.focus() # focuses on entry box so user does not have to click on entry box for every question
        # clears the feedback text
        self.feedback.config(text="")

        # disables generating a new question when the max number of questions has been reached
        if self.question_num > self.max_num:
            self.next_button.config(state=DISABLED)
            self.skip_button.config(state=DISABLED)
            self.question_num_label.config(text="Question {}/{}".format(self.question_num-1, self.max_num))
            self.ask_question.config(text="Well done! You have finished the quiz!") # tells user end of quiz
            self.stats_button.focus()  # focuses on stats button when done

    def check_answer(self):
        # different praises
        praise_list = ["Good job!", "Well done!", "Amazing!", "You did well!",
                       "Fantastic!", "Terrific!"]

        # takes the answer
        self.user_answer = self.answer_entry.get()
        self.user_answer = self.user_answer.lower() # turns entry to lowercase

        # Enter key bind is focused on Next button and unfocused on OK button
        self.next_button.focus()
        self.next_button.bind('<Return>', lambda e:self.generate_ques())
        self.next_button.config(state=NORMAL)# enabled, ready to move to next question


        # if answer is correct
        if self.user_answer == self.answer:
            self.grade += 1 # add a point to grade
            praise = random.choice(praise_list) # randomly picked praises
            self.user_feedback = praise
            self.confirm_button.config(state=DISABLED) # disables while checking so user can't change it
            self.next_button.config(state=NORMAL) # user can only go to the next question if they have answered

        # if answer is blank
        elif self.user_answer == "":
            self.user_feedback = ("Please don't leave it blank!")
            # confirm button does not get disabled here, allows them to guess
            self.next_button.config(state=DISABLED)  # keep next button disabled

        # incorrect answer
        else:
            self.user_feedback = ("Incorrect! The answer was {}.".format(self.answer))
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
