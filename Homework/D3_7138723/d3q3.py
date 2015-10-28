#! /usr/bin/env python3
###############################################################################
#     File Name           :     d3q3.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-28 09:07]
#     Last Modified       :     [2015-10-28 10:35]
#     Description         :     Changes the order of elements in a list
###############################################################################
import sys


def reverseL(L):
    index = 0
    lenL = len(L)
    while index < lenL:
        L.append(L[(lenL-1)-index])
        index += 1
    del L[0:lenL]


s = False

while not s:
    try:
        liste = [int(i) for i in input().split(',')]
        reverseL(liste)
        print(liste)
        s = True
    except ValueError:
        print("Ce programme n'accepte que des nombres entiers pour l'instant.")
    except KeyboardInterrupt:
        print("\n...Aurevoir!")
        sys.exit()
