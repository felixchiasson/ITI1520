#! /usr/bin/env python3
###############################################################################
#     File Name           :     d2q1.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-09 16:05]
#     Last Modified       :     [2015-10-14 12:21]
#     Description         :     Calculer l'indice de masse corporelle
###############################################################################
import sys

def calculBMI(w, h):
    "Retourne l'indice de masse corporelle avec le poids et la hauteur"
    return w / (h * h)

def idealW(weight):
    "Retourne un message basé sur la valeur de weight."
    if weight < 18.5:
        print("Maigreur!")
    elif 18.5 <= weight < 25.0:
        print("Poids idéal!")
    elif 25 <= weight < 30.0:
        print("Surpoids!")
    else:
        print("Obésité!")

positif = False
while not positif:
    try:
        poids = float(input("Veuillez entrer votre poids en kilogrammmes: "))
        taille = float(input("Veuillez entrer votre taille en mètres: "))

        if poids <= 0 or taille <= 0:
            print("Veuillez entrer un nombre positif non nul")

        else:
            bmi = calculBMI(poids, taille)
            print("Votre indice de masse corporelle est", bmi)
            idealW(bmi)
            positif = True      # La boucle arrête

    except ValueError:       # Si l'utilisateur entre une lettre ou un symbol
        print("Vous avez entré un caractère illégal!")
    except KeyboardInterrupt:   # Si l'utilisateur arrête avec ^C
        print("\nAurevoir...!")
        sys.exit()

