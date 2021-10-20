"""
Name: Derek Bolch
lab8.py
"""
from lab7 import encode, encode_better


def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')

    i = 1
    for line in in_file:
        new_line = line.split(' ')
        for word in new_line:
            out_file.write(str(i) + " " + word + "\n")
            i += 1
    in_file.close()
    out_file.close()


def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')

    for line in in_file:
        new_line = line.split(' ')
        new_line[2] = str(float(new_line[2]) + 1.65)
        out_file.write(" ".join(new_line) + "\n")
    in_file.close()
    out_file.close()


def calc_check_sum(isbn):
    isbn = str(isbn)
    total = 0
    for i in range(len(isbn)):
        num = int(isbn[i]) * (10-i)
        total = total + num
    return total % 11


def send_message(file, friend_name):
    in_file = open(file, 'r')
    out_file = open(friend_name + '.txt', 'w')

    for line in in_file:
        out_file.write(line + '\n')
    in_file.close()
    out_file.close()


def send_safe_message(file, friend_name, key):
    in_file = open(file, 'r')
    out_file = open(friend_name + '.txt', 'w')

    for line in in_file:
        new_line = encode(line, key)
        out_file.write(new_line + '\n')

    in_file.close()
    out_file.close()


def send_uncrackable_message(file, friend_name, pad):
    in_file = open(file, 'r')
    pad_file = open(pad, 'r')
    out_file = open(friend_name + '.txt', 'w')

    pad = pad_file.read()
    for line in in_file:
        new_line = encode_better(line, pad)
        out_file.write(new_line + '\n')

    in_file.close()
    out_file.close()


def main():
    # add other function calls here
    number_words('input.txt', 'output.txt')
    hourly_wages('hourly_wages.txt', 'output.txt')
    calc_check_sum('0072946520')
    send_message('jimmy.txt', 'thomas')
    send_safe_message('jimmy.txt', 'thomas', 4)
    send_uncrackable_message('jimmy.txt', 'thomas', 'pad.txt')


main()
