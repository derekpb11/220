"""
Name: Derek Bolch
button.py

Problem: this program will create a class for a button that will be used in three_door_game.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Text
class Button:

    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(self.shape.getCenter(), label)


    def get_label(self):
        return self.text.getText()


    def draw(self, win):
       #  button_rect = self.shape
        self.shape.draw(win)
        self.text.draw(win)


    def undraw(self):
        self.shape.undraw()
        self.text.undraw()


    def is_clicked(self, point):
        rect_p1 = self.shape.getP1()
        rect_p2 = self.shape.getP2()

        if point.getX() >= rect_p1.getX() and point.getX() <= rect_p2.getX():
            if point.getY() >= rect_p1.getY() and point.getY() <= rect_p2.getY():
                return True
        return False


    def color_button(self, color):
        self.shape.setFill(color)


    def set_label(self, label):
        self.text.setText(label)
