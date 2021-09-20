"""
Name: Derek Bolch
traffic.py

Problem: this program will calculate the average number of cars traveled per road

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    # asks user for number of roads
    total_roads = eval(input("How many roads were surveyed? "))
    # starting loop to step though the number of roads
    total_cars = 0
    for i in range(total_roads):
        days_temp = eval(input("How many days was road " + str(i+1) + " surveyed? "))
        cars_acc = 0
        # has user input data on cars traveled each day
        for j in range(days_temp):
            cars_temp = eval(input("How many cars traveled on day " + str(j+1) + "? "))
            cars_acc = cars_acc + cars_temp
        total_cars = total_cars + cars_acc
        road_avg = cars_acc / days_temp
        print("Road ", i, "average vehicles per day: ", round(road_avg, 2))
    print("Total number of vehicles traveled on all roads: ", total_cars)
    total_avg = total_cars / total_roads
    print("Average number of vehicles per road: ", round(total_avg, 2))


if __name__ == "__main__":
    main()
