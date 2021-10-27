"""
Name: Derek Bolch
lab9.py
"""
import math
from graphics import *


def addTen(nums):
    acc = []
    for i in range(len(nums)):
        temp_nums = nums[i]
        temp_nums = temp_nums + 10
        acc.append(temp_nums)
    return acc


def squareEach(nums):
    for i in range(len(nums)):
        temp_nums = math.sqrt(nums[i])


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    return acc


def toNumbers(strList):
    acc = []
    for i in range(len(strList)):
        temp_str = eval(strList[i])
        acc.append(temp_str)


def writeSumOfSquares():
    in_file_name = input("Please enter your input file name: ")
    in_file = open(in_file_name, 'r')
    out_file = open("output.txt", 'w')
    for line in in_file:
        temp_line = toNumbers(line)
        temp_line = sumList(temp_line)
        temp_line = squareEach(temp_line)
        out_file.write("Total of squares =" + str(temp_line) + "\n")


def starter():
    weight = eval(input("Please enter your weight: "))
    wins = eval(input("Please enter your number of wins: "))
    if weight >= 150 and weight < 160 and wins >= 5:
        print("You made the team!")
    elif weight > 199 or wins > 20:
        print("You made the team!")
    else:
        print("Sorry, you didn't make the team")


def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def circleOverlap():
    win = GraphWin("window", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    circle1 = Circle(p1, radius)
    circle1.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()
    radius = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    circle2 = Circle(p1, radius)
    circle2.draw(win)


    circle1_p = circle1.getCenter()
    circle2_p = circle2.getCenter()
    dist = (circle2_p.getX() - circle1_p.getX()) ** 2 + (circle2_p.getY() - circle1_p.getY()) ** 2
    dist = math.sqrt(dist)
    print(dist)
    print(circle1.getRadius())
    print(circle2.getRadius())
    if dist < circle1.getRadius() + circle2.getRadius():
        result_text = Text(Point(200, 200), "The circles overlap")
        result_text.draw(win)
    else:
        result_text = Text(Point(200, 200), "The circles do not overlap")
        result_text.draw(win)
    win.getMouse()
    win.close()


def main():
    # add other function calls here
    # addTen()
    # squareEach()
    # sumList()
    # toNumbers()
    # writeSumOfSquares()
    # starter()
    # leapYear()
    # circleOverlap()

main()