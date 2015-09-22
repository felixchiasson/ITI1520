#! /usr/bin/env python3
###############################################################################
#     File Name           :     l2e4.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-09-22 12:47]
#     Last Modified       :     [2015-09-22 12:55]
#     Description         :     Calcule la surface d'un triangle avec son
#                               périmètre 
###############################################################################
import math
def surfaceTriangle(a, b, c):
    p = a + b + c
    return math.sqrt(p * (p-2*a) * p * (p-2*b) * p * (p-2*c)) / 4

d = float(input("Veuillez entrer le premier coté"))
e = float(input("Veuillez entrer le deuxieme coté"))
f = float(input("Veuillez entrer le troisieme coté"))

print(surfaceTriangle(d, e, f))
