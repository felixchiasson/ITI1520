#! /usr/bin/env python3
###############################################################################
#     File Name           :     l2e3.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-09-22 12:36]
#     Last Modified       :     [2015-09-22 12:42]
#     Description         :     Calcul la note finale 
###############################################################################

def noteFinale(devoirsMoy, partiel, examen):
    return devoirsMoy*0.25 + partiel*0.25 + examen*0.50

devoirs = float(input("Veuillez entrer la moyenne de vos devoirs: "))
partiels = float(input("Veuillez entrer la note de l'examen partiel: "))
examens = float(input("Veuillez entrer la note de l'examen final: "))

print("Votre note final est:", noteFinale(devoirs, partiels, examens))

