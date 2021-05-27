# CSV (component 3) for Animals Quiz
import csv
import random

results = []
with open('animals_quiz(final).csv') as file:

    # make csv file into a list
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        results.append(row)

question_list = random.choice(results) # randomly chooses a row
print(question_list)

question = question_list[0] # adult animal term
answer = question_list[1] # baby animal term
print("The baby term for a {} is a {}".format(question, answer)) # for testing purposes






