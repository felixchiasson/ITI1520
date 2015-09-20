#! /usr/bin/env python3
################################################################################
#     File Name           :     d1q3.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-09-19 15:21]
#     Last Modified       :     [2015-09-19 21:02]
#     Description         :     Converts pounds and ounces to kilograms
################################################################################
import sys

def imperialToMetric(lbs, oz):
    return lbs*0.453592 + oz*0.0283495

positif = False
while not positif:
    try:
        pounds = float(input("Veuillez entrer le nombre de livres: "))
        ounces = float(input("Veuillez entrer le nombre d'onces: "))
    except ValueError:
        print("Vous n'avez pas entré une valeur numérique pour l'une des deux"\
                " options")
        positif = False
    except KeyboardInterrupt:
        sys.exit()
    else:
        if pounds < 0 or ounces < 0:
            print("Votre valeur est négative. Veuillez entrer une valeur"\
                   " positive.")
        else:
            kilograms = imperialToMetric(pounds, ounces)
            print("{0:.1f} livres et {1:.1f} onces équivalent à {2:.4f} "\
                    "kilogrammes.".format(pounds, ounces, kilograms))
            positif = True
