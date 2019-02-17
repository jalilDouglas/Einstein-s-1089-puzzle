
import math

num1 = input("Directions: Choose a three digit number whose first and third digits vary by at least two numbers. I.E 235, 532. ")
#After choosing random number within guidelines
num2 = num1[2] + num1[1] + num1[0]

if int(num1) < int(num2):

            difference = int(num2) - int(num1)
else:

                    difference = int(num1) - int(num2)
#the difference 
newNum1 = str(difference)

newNum2 = newNum1[2] + newNum1[1] + newNum1[0]
# Add the new numer and its reversed number
finish = int(newNum1) + int(newNum2)

print ("If you followed the direcions clearly you should've gotten the number 1089. Your answer was... " ,finish)
Answer ='1089'
if Answer < '1089':
        print ("Your answer Was correct. Good Job!!")
elif Answer > '1089':
    print("Use fewer numbers")
