#! /usr/bin/env python3
###############################################################################
#     File Name           :     l3e4.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-09-29 12:19]
#     Last Modified       :     [2015-09-29 12:32]
#     Description         :     Détermine le nombre de racine réelles pour
#                               une equation
###############################################################################
def nbRacines(a, b, c):
    discriminant = b**2 - 4*a*c
    discriminant = round(discriminant)
    if discriminant == 0:
        racines = 1
    elif discriminant >= 0:
        racines = 2
    else:
        racines = 0
    return racines

a = float(input('Entrez la valeur de a: '))
b = float(input('Entrez la valeur de b: '))
c = float(input('Entrez la valeur de c: '))

resultat = nbRacines(a, b, c)

if resultat == 1:
    print("Il y a une racine réelle (deux identiques)")
elif resultat == 2:
    print("Il y a deux racines distinctes")
elif resultat == 0:
    print("Il n'y a pas de racines réelles")
else:
    print("I don't know")
