"""
Name: Derek Bolch
Partner: <your partner's name goes here – first and last>
lab7.py
"""


def cash_conversion():
    intake = eval(input("Please enter an integer: "))
    print('${}.00'.format(intake))


def encode():
    def encode(message_input, shift):
        final = ''
        for i in range(len(message_input)):
            temp_char = message_input[i]
            temp_ascii = ord(temp_char)
            if temp_ascii >= 122:
                temp_ascii = (temp_ascii + shift) - 26
            elif temp_ascii < 122:
                temp_ascii = (temp_ascii + shift)
                temp_char = chr(temp_ascii)
            final = final + temp_char
        return final


def sphere_area(radius):
    surface_area = 4 * 3.14 * (radius ** 2)
    return surface_area


def sphere_volume(radius):
    volume = (4 / 3) * 3.14 * (radius ** 3)
    return volume


def sum_n(n):
    acc = 0
    for i in range(n):
        acc = acc + i
    acc += n
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc = acc + (i ** 3)
    acc += (n ** 3)
    return acc


def encode_better():
    message = input('Please enter the message you want to encode: ')
    key = input('Please enter the key: ')
    final = ''
    for i in range(len(message)):
        temp_ord_message = ord(message[i])
        shift = ord(key[i]) - 97
        temp_ord_message += shift
        cipher_message = chr(temp_ord_message)
        final += cipher_message
    print(final)


def main():
    # add function calls here
    # cash_conversion()
    # encode()
    # sphere_area()
    # sphere_volume()
    # sum_n()
    # sum_n_cubes()
    # encode_better()
    pass

main()
