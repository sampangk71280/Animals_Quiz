
history = [['giraffe', 'calf'], ['kudu', 'calf'], ['sloth', 'kitten'], ['ferret', 'kit'], ['dolphin', 'calf'], ['deer', 'fawn']]
grade = 4

answer_list = []

for item in history:
    correct_answer = "The baby term for {} is {}!\n".format(item[0], item[1])
    answer_list.append(correct_answer)

print(answer_list)

max_num = 10
percent = grade/max_num * 100
print("{:.0f}".format(percent))

if percent == 100:
    grade_percent = "A+"
elif 89 < percent < 100:
    grade_percent = "A"


final_grade = "Your final grade is {}".format(grade_percent)
print(final_grade)