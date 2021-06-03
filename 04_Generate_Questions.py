# Generate Questions (component 4) for Animals Quiz
import csv
import random

grade = 0
praise_list = ["Good job!", "Well done!", "Amazing!", "You did well!"]
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

# make this into a function
# asks questions
ask = input("What is the baby term for {}?".format(question)).lower()
if ask == answer:
    grade += 1
    praise = random.choice(praise_list)
    print(praise)
elif ask == "":
    print("Please don't leave it blank!")
else:
    print("Incorrect!")







