#! /usr/bin/env python3
###############################################################################
#     File Name           :     l5e2.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-13 11:44]
#     Last Modified       :     [2015-10-13 12:45]
#     Description         :     Retourne la moyenne, min et max des notes. 
###############################################################################
def notes(l):
    # Calcul la moyenne
    somme = 0
    c = 0
    maximum = l[0]
    minimum = l[0]
    while c < len(l):
        somme = l[c] + somme
        c = c + 1 
    for val in l:
        if val > maximum:
            maximum = val

    for i in l:
        if val < minimum:
            minimum = val
    avg = somme / len(l)
    resultats = [avg, minimum, maximum]
    return resultats

inp = input("Veuillez entrer vos notes: ")
liste = list(eval(inp))
results = notes(liste)
print("La moyenne est",results[0],"le minimum est",results[1],"le maximum est",
        results[2])
