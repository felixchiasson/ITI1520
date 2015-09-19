#! /usr/bin/env python3
################################################################################
#     File Name           :     d1q1.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-09-19 15:21]
#     Last Modified       :     [2015-09-19 16:06]
#     Description         :     Converts pounds and ounces to kilograms
################################################################################

positif = False
while not positif:
    try:
        pounds = float(input("Veuillez entrer le nombre de livres: "))
        ounces = float(input("Veuillez entrer le nombre d'onces: "))
    except ValueError:
        print("Vous n'avez pas entré une valeur numérique pour l'une des deux options")
        positif = False
    else:
        if pounds < 0 or ounces < 0:
            print("Votre valeur est négative. Veuillez entrer une valeur positive.")
        else:
            kilograms = pounds*0.453592 + ounces*0.0283495
            print("{} livres et {} onces équivalent à {} kilogrammes.".format(pounds, ounces, kilograms))
            positif = True
