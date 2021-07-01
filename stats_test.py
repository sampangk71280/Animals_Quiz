
history = [['giraffe', 'calf'], ['kudu', 'calf'], ['sloth', 'kitten'], ['ferret', 'kit'], ['dolphin', 'calf'], ['deer', 'fawn']]
grade = 4

answer_list = []

for item in history:
    correct_answer = "The baby term for {} is {}!\n".format(item[0], item[1])
    answer_list.append(correct_answer)

print(answer_list)

