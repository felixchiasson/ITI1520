#! /usr/bin/env python3
###############################################################################
#     File Name           :     l7e2.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-11-03 11:42]
#     Last Modified       :     [2015-11-03 11:47]
#     Description         :     Exercice 2
###############################################################################

def triage(x):
    y = {}
    for i in x:
        y[i] = y.get(i, 0) + 1
    return y
t = (1,2,-3,3,4,-3,3,3)
nombres = triage(t)
nombres_tri = list(nombres.items())
nombres_tri.sort()
print(nombres_tri)

