"""
Name: Derek Bolch
bumper.py

Problem: this program will create a graphical simulation of bumper cars

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint
from math import sqrt
from graphics import Circle, Point, GraphWin, time, color_rgb


def get_random_color():
    rand_1 = randint(0, 255)
    rand_2 = randint(0, 255)
    rand_3 = randint(0, 255)
    return color_rgb(rand_1, rand_2, rand_3)


def get_random(move_amount):
    if move_amount < 0:
        start = move_amount
        end = move_amount * -1
    else:
        start = move_amount * -1
        end = move_amount

    random_num = randint(start, end)
    return random_num


def hit_vertical(ball, win):
    ball = ball.getCenter()
    if ball.getX() < 50 or ball.getX() > (win.getHeight() - 50):
        return True
    return False


def hit_horizontal(ball, win):
    ball = ball.getCenter()
    if ball.getY() < 50 or ball.getY() > (win.getWidth() - 50):
        return True
    return False


def did_collide(ball1, ball2):
    ball1 = ball1.getCenter()
    ball2 = ball2.getCenter()
    dist = (ball2.getX() - ball1.getX()) ** 2 + (ball2.getY() - ball1.getY()) ** 2
    sqrt_dist = sqrt(dist)
    if sqrt_dist < 100:
        return True
    return False


def main():
    # create window
    win_width = 500
    win_height = 500
    win = GraphWin("Bumper", win_width, win_height)

    # pull circle colors
    circle_one_color = get_random_color()
    circle_two_color = get_random_color()
    # create two circles
    circle_one = Circle(Point(100, 250), 50)
    circle_one.setFill(circle_one_color)
    circle_one.setOutline(circle_one_color)
    circle_two = Circle(Point(400, 250), 50)
    circle_two.setFill(circle_two_color)
    circle_two.setOutline(circle_two_color)

    # draw circles
    circle_one.draw(win)
    circle_two.draw(win)

    # create movement
    constant = 1
    x1_direction = get_random(10)
    y1_direction = get_random(10)
    x2_direction = get_random(10)
    y2_direction = get_random(10)
    # while loop to constantly move circles
    while constant > 0:
        circle_one.move(x1_direction, y1_direction)
        circle_two.move(x2_direction, y2_direction)
        time.sleep(0.03)
        # vertical collision checking
        if hit_vertical(circle_one, win):
            x1_direction = x1_direction * -1
        if hit_vertical(circle_two, win):
            x2_direction = x2_direction * -1
        # horizontal collision checking
        if hit_horizontal(circle_one, win):
            y1_direction = y1_direction * -1
        if hit_horizontal(circle_two, win):
            y2_direction = y2_direction * -1
        # collision with each other checking
        if did_collide(circle_one, circle_two):
            x1_direction = x1_direction * -1
            y1_direction = y1_direction * -1
            x2_direction = x2_direction * -1
            y2_direction = y2_direction * -1


if __name__ == "__main__":
    main()
