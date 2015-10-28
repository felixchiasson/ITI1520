#! /usr/bin/env python3
###############################################################################
#     File Name           :     d3q4.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-28 13:55]
#     Last Modified       :     [2015-10-28 14:25]
#     Description         :     Return reversed word and double every letter
###############################################################################

import sys


def stringaroo(string):
    new_string = ''
    index = 0

    while index < len(string):
        new_string = new_string + string[(len(string)-1) - index]*2
        index += 1

    return new_string


print("Veuillez entrer un chaîne de caractères: ")

S = False

while not S:
    try:
        input_string = input()
        print(stringaroo(input_string))
        S = True
    except KeyboardInterrupt:
        print('\n...Aurevoir!')
        sys.exit()
