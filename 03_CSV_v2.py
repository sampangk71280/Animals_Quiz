# CSV (component 3) for Animals Quiz
import csv
import random

results = []
with open('animals_young_quiz.csv') as f:

    # make csv file into a list
    file = csv.reader(f)
    next(f)
    my_list = list(file)

question_ans = random.choice(my_list)
print(question_ans)

question = question_ans[0]
answer = question_ans[1]



