"""
Name: Derek Bolch
vigenere.py

Problem: this program will encode a message given a keyword

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


def code(message, keyword):
    # convert message into usable form
    temp_message = message.replace(" ", "")
    temp_message = temp_message.upper()

    # convert keyword into usable form
    temp_keyword = keyword.upper()
    temp_keyword = temp_keyword * len(message)

    # variables and lists need to encrypt
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    encrypted = ''
    acc = 0

    # for loop to encode
    for i in temp_message:
        shift = alphabet.index(temp_keyword[acc])
        alphabet_num = alphabet.index(i)
        cipher_num = alphabet[(alphabet_num + shift) % 26]
        encrypted = encrypted + cipher_num
        acc = acc + 1
    return encrypted


def main():
    # create window
    win_width = 450
    win_height = 400
    win = GraphWin("Vigenere", win_width, win_height)

    # create text for labels
    message_label = Text(Point(100, 80), "Message to code: ")
    keyword_label = Text(Point(110, 130), "Enter keyword: ")
    message_label.draw(win)
    keyword_label.draw(win)

    # create entry boxes
    message_entry = Entry(Point(285, 82), 24)
    keyword_entry = Entry(Point(240, 132), 14)
    message_entry.draw(win)
    keyword_entry.draw(win)

    # create button and button text
    button = Rectangle(Point(180, 180), Point(270, 230))
    button.draw(win)
    button_text = Text(Point(225, 205), "Encode")
    button_text.draw(win)

    # get text for code function
    win.getMouse()
    message = message_entry.getText()
    keyword = keyword_entry.getText()

    # display results of encode
    result_message = Text(Point(225, 270), "Resulting Message:")
    result_message.draw(win)
    result = Text(Point(225, 288), code(message, keyword))
    result.draw(win)

    # close window text
    close_win = Text(Point(225, 370), "Click anywhere to close window")
    close_win.draw(win)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
