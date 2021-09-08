import math
"""
Name: Derek Bolch
lab2.py
"""


def sum_of_threes():
    upper_bound = eval(input("Enter the upper bound: "))
    acc = 0
    for i in range(0, upper_bound+1, 3):
        acc = acc + i

    print(acc)


def multiplication_table():
    for h in range(1, 11):
        for l in range(1, 11):
            print(h*l, end=" ")
        print()


def triangle_area():
    side_a = eval(input("Enter the a value: "))
    side_b = eval(input("Enter the b value: "))
    side_c = eval(input("Enter the c value: "))

    s = (side_a + side_b + side_c) / 2
    triangle_area = math.sqrt(s*(s-side_a)*(s-side_b)*(s-side_c))
    print(triangle_area)


def sum_squares():
    lower_range = eval(input("Enter the lower value: "))
    upper_range = eval(input("Enter the upper value: "))
    squared_output = 0
    for i in range(lower_range, upper_range+1):
        squared_output += i ** 2

    print(squared_output)


def power():
    base = eval(input("Enter the base value: "))
    exponent = eval(input("Enter the exponent value: "))
    power_acc = 1
    for i in range(exponent):
        power_acc = power_acc * base

    print(base, " ^ ", exponent, " = ", power_acc)


sum_of_threes()
# multiplication_table()
# triangle_area()
# sum_squares()
# power()
