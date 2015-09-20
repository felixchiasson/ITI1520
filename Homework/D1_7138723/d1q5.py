#! /usr/bin/env python3
###############################################################################
#     File Name           :     d1q5.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-09-19 21:09]
#     Last Modified       :     [2015-09-19 22:31]
#     Description         :     Convertit une valeur en année-lumière en
#                               secondes et en distance et compare la distance
#                               entre deux étoiles données en année-lumière.
###############################################################################
import sys

def convSecondes(a):
        return a * 365.26 * 86400

def convKm(s):
        return s * 300000

def calcDist(e, f):
    if e > f:
        return convKm(convSecondes(e)) - convKm(convSecondes(f))
    else:
        return convKm(convSecondes(f)) - convKm(convSecondes(e))

positif = False
s = False

while not positif:
    try:
        nbAL = float(input("Entrez le nombre d'années-lumières: "))
        if nbAL >= 0:
            nbSec = convSecondes(nbAL)
            distance = convKm(nbSec)
            print("Le nombre de secondes lumières est de: {0:.1f} "\
                    "secondes.".format(nbSec))
            print("La distance est: {0:.1f}km".format(distance))
            positif = True
        else:
            print("Il est impossible de de retourner dans le temps. "\
                    "Veuillez réessayer.")
    except ValueError:
        print("Veuillez entrer une valeur numérique.")

    except KeyboardInterrupt:
        print("\nAurevoir...")
        sys.exit()

while not s:
    try:
        etoileA = float(input("Entrez la distance de la première étoile, en "\
                "années-lumières: "))
        etoileB = float(input("Entrez la distance de la deuxième étoile, en "\
                "années-lumières: "))
        if etoileA >=0 and etoileB >=0:
            distanceB = calcDist(etoileA, etoileB)
            print("La distance entre les deux étoiles est {0:.1f} "\
                    "km".format(distanceB))

            s = True

        else:
            print("Il est impossible de retourner dans le temps. Veuillez "\
                    "réessayer.")

    except ValueError:
        print("Veuillez entrer une valeur numérique.")

    except KeyboardInterrupt:
        print("\nAurevoir...")
        sys.exit()
