#! /usr/bin/env python3
###############################################################################
#     File Name           :     d3q3.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-28 09:07]
#     Last Modified       :     [2015-10-28 14:23]
#     Description         :     Changes the order of elements in a list
###############################################################################
import sys


def reverse_list(L):
    index = 0
    len_list = len(L)
    while index < len_list:
        L.append(L[(len_list-1)-index])
        index += 1
    del L[0:len_list]


s = False

print("Veuillez entrer des nombres séparés par des virgules.")

while not s:
    try:
        liste = [int(i) for i in input().split(',')]
        reverse_list(liste)
        print(liste)
        s = True
    except ValueError:
        print("Ce programme n'accepte que des nombres entiers pour l'instant.")
    except KeyboardInterrupt:
        print("\n...Aurevoir!")
        sys.exit()
