"""
Name: Derek Bolch
mean.py

Problem: this program displays three different methods for calculating a mean of a set of numbers.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def main():

    # takes user input
    num_inputs = eval(input("Please enter the number of inputs: "))
    # asks user for dataset
    num_list = []
    for i in range(num_inputs):
        input_temp = eval(input("Enter value " + str(i+1) + ":"))
        num_list.append(input_temp)
    # converts the list of strings into a list of ints
    for i in range(num_inputs):
        num_list[i] = int(num_list[i])

    # rms_average loop
    rms_acc = 0
    for i in range(num_inputs):
        rms_acc = rms_acc + (num_list[i] ** 2)

    rms_average = rms_acc / num_inputs
    rms_average = math.sqrt(rms_average)

    # harmonic_mean loop
    hrm_acc = 0
    for i in range(num_inputs):
        hrm_acc = hrm_acc + (1 / num_list[i])

    hrm_mean = num_inputs / hrm_acc

    # geometric_mean loop
    geo_acc = 1
    for i in range(num_inputs):
        geo_acc = geo_acc * (num_list[i])

    geo_mean = geo_acc ** (1 / num_inputs)

    # Final values printed
    print(round(rms_average, 3))
    print(round(hrm_mean, 3))
    print(round(geo_mean, 3))


if __name__ == "__main__":
    main()
