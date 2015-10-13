#! /usr/bin/env python3
###############################################################################
#     File Name           :     l5e4.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-13 12:12]
#     Last Modified       :     [2015-10-13 13:26]
#     Description         :     Calcul l'écart type 
###############################################################################
from math import sqrt

def ecartTyp(l):
    i = 0
    somm = 0
    while i < len(l)
        somm = somm + 1
        i = i + 1

    a = somm / len(l)
    h = 0
    compteur = 0
    while compteur < len(l):
        h = h + (l[compteur] - a)**2
        compteur = compteur + 1
    s = sqrt(h/(len(l)-1))
    return s

inp = input("Veuillez entrer vos valeurs séparées par des virgules: ")
liste = list(eval(inp))
ecart = ecartTyp(liste)
print("L'écart type est", ecart)


