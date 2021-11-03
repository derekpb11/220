"""
Name: Derek Bolch
lab3.py
"""
# comment

def average():
    grade_num = eval(input("Please enter the number of grades you want to average:  "))
    avg_acc = 0

    for i in range(grade_num):
        avg_temp = eval(input("Enter your grade on HW " + str(i+1) + ":"))
        avg_acc = avg_acc + avg_temp

    print(avg_acc / grade_num)


def tip_jar():
    tip_acc = 0
    for i in range(5):
        tip_temp = eval(input("Enter the amount put into the jar: "))
        tip_acc = tip_acc + tip_temp

    print("The total donations are:", tip_acc)


def newton():
    x = eval(input("please enter the number that you want to approximate: "))
    refine = eval(input("Please enter the number of times you want to improve your approximation: "))
    approx_acc = x / 2
    for i in range(refine):
        approx_acc = (approx_acc + (x / approx_acc)) / 2

    print(approx_acc)


def sequence():
    x = eval(input("Please enter the number of terms: "))
    for i in range(x+1):
        x = 1 + (i // 2 * 2)
        print(x, end=" ")


def pi():
    n = eval(input("Please enter the number of terms in the series: "))
    acc_pi = 1
    for i in range(n):
        num = 2 + (i // 2 * 2)
        denom = 1 + ((i + 1) // 2 * 2)
        acc_pi = acc_pi * (num / denom)

    print(acc_pi * 2)


# average()
# tip_jar()
# newton()
sequence()
# pi()
