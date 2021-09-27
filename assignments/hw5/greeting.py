"""
Name: Derek Bolch
greeting.py

Problem: this program will display a fun greeting card

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import GraphWin, Polygon, Point, Circle, Line, Text, time


def main():

    # create window
    height = 500
    width = 500
    win = GraphWin("Greeting Card", width, height)
    # create triangle for heart
    l_tri = Polygon(Point(250, 400), Point(100, 190), Point(250, 100))
    r_tri = Polygon(Point(250, 400), Point(400, 190), Point(250, 100))
    l_tri.setFill("red")
    l_tri.setOutline("red")
    r_tri.setFill("red")
    r_tri.setOutline("red")
    r_tri.draw(win)
    l_tri.draw(win)

    # draw circles for heart
    l_circ = Circle(Point(175, 145), 87)
    r_circ = Circle(Point(325, 145), 87)
    l_circ.setFill("red")
    l_circ.setOutline("red")
    r_circ.setFill("red")
    r_circ.setOutline("red")
    l_circ.draw(win)
    r_circ.draw(win)

    # draw arrow
    arrow_point = Polygon(Point(70, 430), Point(52, 445), Point(68, 455))
    arrow_point.setFill("grey")
    arrow_point.setOutline("grey")
    arrow_point.draw(win)
    arrow_stem = Line(Point(61, 448), Point(43, 480))
    arrow_stem.setWidth(3)
    arrow_stem.setFill("brown")
    arrow_stem.draw(win)

    # Greeting text and instruction text
    greeting = Text(Point(250, 35), "Happy Valentine's Day!")
    instruction = Text(Point(250, 450), "Click to shoot arrow")
    greeting.draw(win)
    instruction.draw(win)
    win.getMouse()

    # shoot arrow
    for _ in range(60):
        arrow_point.move(6, -7)
        arrow_stem.move(6, -7)
        time.sleep(0.03)

    # change text
    instruction.undraw()
    close = Text(Point(250, 450), "Click again to close window")
    close.draw(win)
    win.getMouse()


if __name__ == "__main__":
    main()
