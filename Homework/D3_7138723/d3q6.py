#! /usr/bin/env python3
###############################################################################
#     File Name           :     d3q6.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-11-01 18:37]
#     Last Modified       :     [2015-11-01 19:27]
#     Description         :     Convert roman numeral to arabic numerals
###############################################################################

import sys


def romaine_v1(string):

    string = string.strip()
    string = string.lower()

    nombre_M = string.count('m') * 1000
    nombre_D = string.count('d') * 500
    nombre_C = string.count('c') * 100
    nombre_X = string.count('x') * 10
    nombre_V = string.count('v') * 5
    nombre_i = string.count('i') * 1

    return nombre_M + nombre_D + nombre_C + nombre_X + nombre_V + nombre_i


def romaine_v2(string):

    total = 0

    for y in string:

        if y == 'm' or y == 'M':
            total += 1000
        elif y == 'd' or y == 'D':
            total += 500
        elif y == 'c' or y == 'C':
            total += 100
        elif y == 'x' or y == 'X':
            total += 10
        elif y == 'v' or y == 'V':
            total += 5
        elif y == 'i' or y == 'I':
            total += 1
        else:
            return False

    return total


s = False

print('Veuillez enter une combinaison de chiffres romains (M, D, C, X, V, I)')

while not s:
    try:
        roman_input = input()
        romaine_1 = romaine_v1(roman_input)
        romaine_2 = romaine_v2(roman_input)

        if romaine_2 is not False:

            print('Avec la fonction romaine_v1:', romaine_v1(roman_input))
            print('Avec la fonction romaine_v2:', romaine_v2(roman_input))
            s = True

        else:
            raise ValueError

    except ValueError:
        print('Veuillez entrer une combinaison de M, D, C, X, V et I sans'
              ' espaces à la fin.')
    except KeyboardInterrupt:
        print('\n...Aurevoir!')
        sys.exit()
