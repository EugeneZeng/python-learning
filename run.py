# encoding: utf-8
import plus
import random

def testStatements(statements):
    random.shuffle(statements)
    for statement in statements:
        sum = input(str(statement[0]) + " + " + str(statement[1]) + " = ")
        if int(sum) != statement[2]:
            print("incorrect! should be ", statement[2])
        else:
            print("correct!")

print("Please choose the type: \n", end=" ")
print("1. plus inner 10\n", end=" ")
print("2. plus inner 20\n")
type = input("Please enter the number: ")


if type == "1":
    testStatements(plus.getSumBelow(10))
elif type == "2":
    testStatements(plus.getBelow(10))
else:
    print("[ERROR] invalid input...")