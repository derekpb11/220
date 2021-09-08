"""
Name: Derek Bolch
lab1.py

Problem: This function calculates the area of a rectangle
"""

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length_v =  eval(input("Enter the length: "))
    width_v =  eval(input("Enter the width: "))
    height_v =  eval(input("Enter the depth: "))
    volume = length_v * width_v * height_v
    print("Volume =", volume)


def shooting_percentage():
    total_shots = eval(input("Enter the total shots taken: "))
    shots_made = eval(input("Eneter the total shots made: "))
    percent_made = 100 * (shots_made / total_shots)
    print("Shooting percentage =", percent_made)


def coffee():
    pounds = eval(input("Enter the number of pounds ordered: "))
    total_cost = 1.50 + (10.50 * pounds) + (0.86 * pounds)
    print("The total cost of your order is:", total_cost)


def kilometers_to_miles():
    k_to_m = eval(input("Enter the number of kilometers traveled: "))
    miles = k_to_m / 1.61
    print("Miles traveled:", miles)


calc_rec_area()
#calc_volume()
#shooting_percentage()
#coffee()
#kilometers_to_miles()



