#ABDUL MUNEEB SYED
#8/8/2022
#Problem 5: Search the internet for how to convert radians to degrees. Write a program to compute the conversion given a user input value. Print this value as well as the calculated value using the degrees function in the math module.



#Import math
import math
#ask the user input
radian = int(input("What's the radian value?"))
#formula to calculate degree
degree = (radian*180)/math.pi
#printing degree
print(degree)
