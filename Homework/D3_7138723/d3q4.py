#! /usr/bin/env python3
###############################################################################
#     File Name           :     d3q4.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-28 13:55]
#     Last Modified       :     [2015-11-01 22:15]
#     Description         :     Return reversed word and double every letter
###############################################################################

import sys


def stringaroo(string):
    """
    Reverse a string, double each letter, and return a string
    """

    new_string = ''
    index = 0

    while index < len(string):
        # Add the last element minus the current value of index to the string
        new_string = new_string + string[(len(string)-1) - index]*2
        index += 1

    return new_string


print("Veuillez entrer un chaîne de caractères: ")

s = False

while not s:
    try:
        input_string = input()
        print(stringaroo(input_string))
        s = True

    # If user quits early with ^C
    except KeyboardInterrupt:
        print('\n...Aurevoir!')
        sys.exit()
