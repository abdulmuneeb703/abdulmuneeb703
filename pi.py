#ABDUL MUNEEB SYED
#8/8/2022
#Problem 4:  Search on the internet for a way to calculate an approximation for pi. There are many that use simple arithmetic. Write a program to compute the approximation and then print that value as well as the value of math.pi from the math module.

# Initialize denominator
M = 1

# Initialize sum
R = 0

for i in range(1000000):

    # even index elements are positive
    if i % 2 == 0:
        R += 4 / M
    else:

        # odd index elements are negative
        R -= 4 / M

    # denominator is odd
    M += 2

print(R)

#Importing math
import math

print(math.pi)
