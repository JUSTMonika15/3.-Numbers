"""CSC 161 Lab: Numbers

Lihang Liu
Lab Section TR 2:00-3:15pm
Spring 2022
"""

import math


def main():
    print("This program calculate the square root of a given number using the secant method.")
    num = float(input("What is the number for which you want to calculate the square root? "))
    times = float(input("How many iterations do you want to use? "))
    x0 = num/5
    x1 = num/10
    for i in range(int(times)):
        aprox = x0 - ((x0 ** 2) - num)/(x0 + x1)
        x0 = aprox
        x1 = x0
        print(str(i + 1) + " " + str(aprox) + " " + str((aprox) - math.sqrt(num)))
    print("My guess for the square root of " + str(num) + " is " + str(aprox))
    print("The difference between my guess and the real result is" + (str((aprox) - math.sqrt(num))))


if __name__ == '__main__':
    main()
