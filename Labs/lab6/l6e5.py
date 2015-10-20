#! /usr/bin/env python3
################################################################################
#     File Name           :     l6e5.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-20 12:55]
#     Last Modified       :     [2015-10-20 13:26]
#     Description         :     ehhhhh
################################################################################

def espaces(L):
    mot = ''
    for c in L:
        mot = mot + c + ' '
    mot = mot.strip()
    return mot

L = input('Inserez le mot: ')
print(espaces(L))
