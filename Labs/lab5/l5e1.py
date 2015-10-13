#! /usr/bin/env python3
###############################################################################
#     File Name           :     l5e1.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-13 11:35]
#     Last Modified       :     [2015-10-13 12:46]
#     Description         :     Obtient une liste de valeurs et fait la moyenne 
###############################################################################

def listAvg(l):
    somme = 0
    c = 0
    while c < len(l):
        somme = l[c] + somme
        c = c + 1

    moyenne = somme / len(l)
    return moyenne

imp = input("Entrez chaque chiffre séparé par des virgules: ")
liste = list(eval(imp))
moy = listAvg(liste)
print("La moyenne est",moy)
