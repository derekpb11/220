"""
Name: Derek Bolch
lab5.py
"""
import math
from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    user_shape = Polygon(p1, p2, p3)
    user_shape.draw(win)

    # and display its area/perimeter in the graphics window.
    line_1 = math.sqrt(abs(p1.getX() - p2.getX()) ** 2 + abs(p1.getY() - p2.getY()) ** 2)
    line_2 = math.sqrt(abs(p2.getX() - p3.getX()) ** 2 + abs(p2.getY() - p3.getY()) ** 2)
    line_3 = math.sqrt(abs(p3.getX() - p1.getX()) ** 2 + abs(p3.getY() - p1.getY()) ** 2)
    perimeter = line_1 + line_2 + line_2
    p = perimeter / 2
    area = math.sqrt(p * (p - line_1) * (p - line_2) * (p - line_3))

    # draw text
    inst_pt = Point(200, 400)
    text_area = Text(inst_pt, "The area is: " + str(round(area, 3)))
    text_area.draw(win)

    inst_pt = Point(200, 430)
    text_perimeter = Text(inst_pt, "The perimeter is: " + str(round(perimeter, 3)))
    text_perimeter.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    # write code here
    # create entry boxes
    red_box = Entry(Point(200, 240), 5)
    green_box = Entry(Point(200, 270), 5)
    blue_box = Entry(Point(200, 300), 5)

    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)

    # for loop for changing color
    for i in range(5):
        win.getMouse()
        red = int(red_box.getText())
        green = int(green_box.getText())
        blue = int(blue_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    user_string = input("Please enter a string: ")
    # step 1
    print(user_string[0])
    # step 2
    print(user_string[-1])
    # step 3
    print(user_string[2:6])
    # step 4
    print(user_string[0] + user_string[-1])
    # step 5
    print(user_string[:3] * 10)
    # step 6
    for i in range(len(user_string)):
        indiv = user_string[i]
        print(indiv)
    # step 7
    print(len(user_string))


def process_list():

    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    #step 1
    x = values[1] + values[3]
    print(x)
    # step 2
    x = values[0] + values[2]
    print(x)
    # step 3
    x = values[1] * 5
    print(x)
    # step 4
    x = [values[2], values[3], values[4]]
    print(x)
    # step 5
    x = [values[2], values[3], values[0]]
    print(x)
    # step 6
    x = [values[2], values[0], float(values[5])]
    print(x)
    # step 7
    x = values[0] + values[2] + float(values[5])
    print(x)
    # step 8
    print(len(values))


def another_series():
    user_series = eval(input("Please enter the number of terms: "))
    acc = 0
    for i in range(user_series):
        y = 2 + 2 * (i % 3)
        acc += y
        print(y)
    print("sum = ", acc)



def main():
    # target()
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()


main()
