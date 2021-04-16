from elGamal import Couple


def string_to_list(string):
    letter_list = []
    for i in string:
        letter_list.append(ord(i))
    return letter_list


def list_to_string(letter_list):
    string = ''
    for i in letter_list:
        string += chr(i)
    return string


def cipher_to_string(cipher_list):
    string = ''
    for i in cipher_list:
        string += format(i.a) + ' ' + format(i.b) + ' '
    string = string[0:-1]
    return string


def string_to_cipher(string):
    flag = True
    cipher_list = []

    string_list = string.split(' ')
    for i in string_list:
        if flag:
            a = int(i)
            flag = not flag
        else:
            b = int(i)
            cipher_list.append(Couple(a, b))
            flag = not flag
    return cipher_list
