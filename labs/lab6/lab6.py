"""
Name: Derek Bolch
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    user_name = input('Please enter your first and last name: ')
    name_list = user_name.split(" ")
    print(name_list[1] + ", " + name_list[0])


def company_name():
    url = input('Please enter a three-part internet domain name:')
    url_list = url.split(".")
    print(url_list[1])


def initials():
    num_names = eval(input('Please enter the number of names that you want to enter: '))

    for i in range(num_names):
        temp_first = input('Please enter the first name of student ' + str(i+1) + ':')
        temp_last = input('Please enter ' + temp_first + "'s last name: ")
        temp_initials = temp_first[0] + temp_last[0]
        print(temp_first + "'s initials are " + temp_initials)


def names():
    names_input = input('Please enter a list of names separated by a comma and a space: ')
    names_list = names_input.split(", ")
    final_initials = 'The initials are '

    for i in names_list:
        temp_list = i.split(" ")
        temp_first = temp_list[0]
        temp_last = temp_list[1]
        temp_initials = temp_first[0] + temp_last[0]
        final_initials = final_initials + temp_initials + " "

    print(final_initials)


def thirds():
    num_sentences = eval(input('Please enter the number of sentences that will be input: '))

    for i in range(num_sentences):
        temp_sentence = input('Please enter sentence ' + str(i+1) + ': ')
        every_third = temp_sentence[2:len(temp_sentence):3]
        print(every_third)


def word_average():
    user_input = input('Please enter the sentence you want to average the word length: ')
    input_list = user_input.split(" ")
    acc = 0
    for word in input_list:
        acc = acc + len(word)

    word_avg = acc / len(input_list)
    print("average word length: ", word_avg)


def pig_latin():
    user_input = input('Please enter the sentence you want to convert to pig latin: ')
    user_input = user_input.lower()
    words = user_input.split(" ")
    acc = ''
    for word in words:
        acc = acc + word[1:] + word[0] + "ay "

    print(acc)


def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()
    # add other function calls here


main()
