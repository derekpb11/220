"""
Name: Derek Bolch
button.py

Problem: this program will create a class for a button that will be used in three_door_game.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Text
class Button:
    """
    Class to create buttons that will be used in three_door_game.py
    """

    def __init__(self, shape, label):
        """
        Constructor method to create Button object, requires shape as a Rectangle object
        and label as a string.
        """
        self.shape = shape
        self.text = Text(self.shape.getCenter(), label)


    def get_label(self):
        """
        Method that will return the label of the button object
        """
        return self.text.getText()


    def draw(self, win):
        """
        Method to draw the button rectangle and label text
        """
        self.shape.draw(win)
        self.text.draw(win)


    def undraw(self):
        """
        Method to undraw the button rectangle and label text
        """
        self.shape.undraw()
        self.text.undraw()


    def is_clicked(self, point):
        """
        Method to determine if user clicks on button, returns true if yes, false if no
        """
        rect_p1 = self.shape.getP1()
        rect_p2 = self.shape.getP2()

        if point.getX() >= rect_p1.getX() and point.getX() <= rect_p2.getX():
            if point.getY() >= rect_p1.getY() and point.getY() <= rect_p2.getY():
                return True
        return False


    def color_button(self, color):
        """
        Method to change the color of the button to the sting color
        """
        self.shape.setFill(color)


    def set_label(self, label):
        """
        Method to set the label text to the label string parameter
        """
        self.text.setText(label)
