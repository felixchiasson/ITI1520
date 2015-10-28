#! /usr/bin/env python3
###############################################################################
#     File Name           :     d3q4.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-28 13:55]
#     Last Modified       :     [2015-10-28 14:05]
#     Description         :     Return reversed word and double every letter
###############################################################################

import sys


def stringaroo(string):
    newString = ''
    index = 0

    while index < len(string):
        newString = newString + string[(len(string)-1) - index]*2
        index += 1

    return newString


print("Veuillez entrer un chaîne de caractères: ")

S = False

while not S:
    try:
        inputString = input()
        print(stringaroo(inputString))
        S = True
    except KeyboardInterrupt:
        print('\n...Aurevoir!')
        sys.exit()
