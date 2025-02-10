import random as r
answers = []
with open("answers.txt", "r") as inputfile:
    for line in inputfile:
        answers.append(line)
input("Magic 8-Ball, Think of a question and press enter.")
num = r.randint(1,20)
print(answers[num])


