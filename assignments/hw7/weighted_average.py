"""
Name: Derek Bolch
weighted_average.py

Problem: this program will calculate the weighted average from a dataset

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    # open files
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')

    # split file into individual people
    input_list = []
    for line in in_file.readlines():
        input_list.append(line[:])

    # main for loop to go though splits and conversions
    for i in range(len(input_list)):
        split_name = input_list[i].split(":")
        temp_name = split_name[0]
        temp_values = split_name[1]
        value_list = temp_values.split(" ")
        value_list.remove('')
        # converts values from string to int
        for p in range(0, len(value_list)):
            value_list[p] = int(value_list[p])

        # create variables for item lists
        weight_list = []
        grade_list = []
        for _ in range(len(input_list)):
            weight_list = value_list[0:-1:2]
            grade_list = value_list[1::2]

        # calculated the weighted average
        acc = 0
        for j in range(len(weight_list)):
            acc = acc + int((weight_list[j]) * int(grade_list[j]))
        acc = round(acc/100, 1)
        # create returned string (each line will become part of a list)
        final_output = temp_name + "'s average: " + str(acc)
        # print(final_output, file=out_file)

        # If statement for if the weight adds up to 100 or not
        weight_acc = 0
        for k in range(len(weight_list)):
            weight_acc += weight_list[k]

        if weight_acc > 100:
            print(temp_name + "'s average: Error: The weights are more than 100.", file=out_file)
        elif weight_acc < 100:
            print(temp_name + "'s average: Error: The weights are less than 100.", file=out_file)
        else:
            print(final_output, file=out_file)

    in_file.close()
    out_file.close()


def main():
    weighted_average('grades.txt', 'avg.txt')


if __name__ == "__main__":
    main()
