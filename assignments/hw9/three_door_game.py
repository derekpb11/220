"""
Name: Derek Bolch
three_door_game.py

Problem: this program will create a secret door game based off of the the button class

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import GraphWin, Rectangle, Point, Text
from button import Button



def main():
    win = GraphWin("win", 600, 400)
    # create buttons
    but1 = Button(Rectangle(Point(100, 200), Point(175, 275)), "Door 1")
    but1.draw(win)

    but2 = Button(Rectangle(Point(250, 200), Point(325, 275)), "Door 2")
    but2.draw(win)

    but3 = Button(Rectangle(Point(400, 200), Point(475, 275)), "Door 3")
    but3.draw(win)

    # create top text
    top_text = Text(Point(300, 100), "I have a secret door")
    top_text.draw(win)

    # create bottom text
    bottom_text = Text(Point(300, 375), "Click to choose my door")
    bottom_text.draw(win)

    # choose door
    my_door = randint(1, 3)
    click = win.getMouse()
    if but1.is_clicked(click):
        if my_door == 1:
            but1.color_button("green")
            top_text.setText("You Win!")
            bottom_text.setText("Click to close")
        else:
            but1.color_button("red")
            top_text.setText("You Lost!")
            bottom_text.setText("Door " + str(my_door) + " is my secret door")

    if but2.is_clicked(click):
        if my_door == 2:
            but2.color_button("green")
            top_text.setText("You Win!")
            bottom_text.setText("Click to close")
        else:
            but2.color_button("red")
            top_text.setText("You Lost!")
            bottom_text.setText("Door " + str(my_door) + " is my secret door")

    if but3.is_clicked(click):
        if my_door == 3:
            but1.color_button("green")
            top_text.setText("You Win!")
            bottom_text.setText("Click to close")
        else:
            but3.color_button("red")
            top_text.setText("You Lost!")
            bottom_text.setText("Door " + str(my_door) + " is my secret door")

    win.getMouse()


if __name__ == "__main__":
    main()
