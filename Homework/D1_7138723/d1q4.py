#! /usr/bin/env python3
################################################################################
#     File Name           :     d1q4.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-09-19 16:36]
#     Last Modified       :     [2015-09-19 20:59]
#     Description         :     Calcule le nombre minimal de pièce de monnaie 
#                               nécessaire pour une valeur en $ donnée.
################################################################################
import sys

def piecesMin(amount):
    qM = amount % 0.25
    nbQ = amount // 0.25i

    nbD = qM // 0.10
    dM = round(qM, 2) % 0.10

    nbN = dM // 0.05
    nM = round(dM,2) % 0.05
        
    nbP = nM // 0.01
    pM = round(nM,2) % 0.01

    return nbQ + nbD + nbN + nbP

positif = False
while not positif:
    try:
        montant = float(input('Entrez le montant en dollars: '))
    except ValueError:
        print("Veuillez entrer une valeur numérique.")
        positif = False
    except KeyboardInterrupt:
        sys.exit()
    else:

        if montant < 0:
            print("Veuillez entrer une valeur numérique positive.")
        else:
            nbMin = piecesMin(montant)
            print("Le caissier aura besoin d'un minimum de {0:.0f}"\
                    "pièces.".format(nbMin))
            positif = True

