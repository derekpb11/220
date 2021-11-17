"""
Name: Derek Bolch
lab12.py
"""
from random import randint


def find_and_remove_first(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Derek"
    except:
        pass


def read_data(filename):
    f = open(filename, "r")
    d = f.readline()
    d.split(" ")
    i = 0
    while i < len(d):
        for i in range(len(d)):
            d = int(d[i])
        i += 1
    return d


def is_in_linear(search_val, lst):
    i = 0
    while i <= len(lst):
        if lst[i] == search_val:
            return True
        i += 1


def good_input():
    x = eval(input("Please enter an input: "))
    while x <= 10 and x >= 1:
        x = eval(input("Input was not within the range 1-10, please enter again: "))
    return x


def num_digits():
    x = eval(input("Please enter a positive integer: "))
    while x > 0:
        i = 0
        while x > 0:
            i += 1
            x //= 10
        print("The number of digits is", x)
        x = eval(input("Please enter a positive integer: "))


def hi_lo_game():
    number = randint(1, 100)
    guesses = 0
    x = eval(input("Please guess a number between 1 and 100:"))
    while guesses < 7 and x != number:
        if x > number:
            print("Number is too high")
            x = eval(input("Please guess a number between 1 and 100:"))
        elif x < number:
            print("Number is too low")
            x = eval(input("Please guess a number between 1 and 100:"))
            guesses += 1
    if x == number:
        print("You won in", guesses, "guesses")
    else:
        print("Sorry you lose. the number was", number)


def main():
    # add other function calls here
    find_and_remove_first()
    read_data("dataSorted.txt")
    is_in_linear()
    good_input()
    num_digits()
    hi_lo_game()


main()
