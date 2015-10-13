#! /usr/bin/env python3
###############################################################################
#     File Name           :     l5e3.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-13 11:53]
#     Last Modified       :     [2015-10-13 13:29]
#     Description         :     Calcule la distance  
###############################################################################
from math import pi, cos, sin

def distance(v):
    resultats = []
    for i in range(0, 100, 10):
        a = (pi/180)*i
        d = ((2*(v**2)) * cos(a) * sin(a))/9.8
        resultats.append(d)
    return resultats

inp = float(input("vitesse: "))
reponse = distance(inp)
for i in range(0,10):
    print("Pour", i*10,"la réponse est:",
            reponse[i])

