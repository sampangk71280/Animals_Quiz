# Generate Questions (component 4) for Animals Quiz
import csv
import random

def input_checker():
    input("What is the baby term for a {}?".format(question).lower())



# grade points
grade = []

# list for animal adult and baby term
results = []
with open('animals_young_quiz.csv') as file:

    # make csv file into a list
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        results.append(row)

question_list = random.choice(results) # randomly chooses a row
print(question_list)

question = question_list[0] # adult animal term
answer = question_list[1] # baby animal term








