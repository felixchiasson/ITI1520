#! /usr/bin/env python3
###############################################################################
#     File Name           :     l3e3.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-09-29 12:12]
#     Last Modified       :     [2015-09-29 12:18]
#     Description         :     Détermine si un entier est divisible par 2 ou 3 
###############################################################################

def estDivisible(entier):
    if entier % 2 == 0 and entier % 3 == 0:
        divisible = 1
    elif entier % 2 == 0 or entier % 3 == 0:
        divisible = 2
    else:
        divisible = 0
    return divisible

entier = int(input("Entrez un nombre entier: "))

divi = estDivisible(entier)

if divi == 1:
    print("L'entier est divisible par 2 et 3")
elif divi == 2:
    print("L'entier est divisible par 2 ou 3")
elif divi == 0:
    print("L'entier n'est pas divisible ni par 2 ni par 3")
else:
    print("Aucune idée!")

