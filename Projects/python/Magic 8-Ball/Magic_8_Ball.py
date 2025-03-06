import random as r

with open("answers.txt", "r") as inputfile:
    answers = [line for line in inputfile]

input("Magic 8-Ball, Think of a question and press enter.")
num = r.randint(1,20)
print(answers[num])


