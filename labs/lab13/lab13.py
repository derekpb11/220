"""
Name: Derek Bolch
lab13.py
"""


def is_in_binary(search_val, values):
    mid = values[len(values)//2]
    while mid != search_val and len(values) != 1:
        if search_val > mid:
            values = values[:mid]
        else:
            values = values[mid+1:]
    mid = values[len(values) // 2]
    if mid == search_val:
        return True
    else:
        return False


def select_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i, len(values)):
            if j < lowest:
                lowest = values[pos]
                pos = j
        values[i], values[j] = values[i], values[i]


def get_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    w = abs(p1.getX() - p2.getX())
    h = abs(p1.getY() - p2.getY())
    return w * h


def rectangles(values):
    d = {}
    areas = []
    for rect in values:
        d[get_area(rect)] = rect
        areas.append(get_area(rect))
    select_sort(areas)
    for i in range(len(areas)):
        values[i] = d[i]
    print(areas)


# Capstone problem here

def trade_alert(filename):
    infile = open(filename, "r")
    data = infile.read().split()
    int_data = []
    for i in range(len(data)):
        int_data.append(int(data[i]))
    for j in range(len(int_data)):
        second = j
        if int_data[j] > 830:
            print("Warning! volume exceeds 830 at second", second)
        elif int_data[j] > 500:
            print("Alert! volume exceeds 500 at second", second)


def main():
    # add other function calls here
    ss_list = [3, 4, 5, 2, 1]
    binary_list = [1, 2, 3, 4, 5]
    is_in_binary(3, binary_list)
    select_sort(ss_list)
    trade_alert("trades.txt")


main()
