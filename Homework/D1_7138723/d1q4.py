#! /usr/bin/env python3
################################################################################
#     File Name           :     d1q4.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-09-19 16:36]
#     Last Modified       :     [2015-10-03 10:32]
#     Description         :     Calcule le nombre minimal de pièce de monnaie 
#                               nécessaire pour une valeur en $ donnée.
################################################################################
import sys

def piecesMin(amount):                  # Fonction qui calcule le nombre
    qM = amount % 0.25                  # minimal de pièces nécessaires
    qM = round(qM, 2)
    nbQ = amount // 0.25

    nbD = qM // 0.10
    dM = qM % 0.10
    dM = round(dM, 2)

    nbN = dM // 0.05
    nM = dM % 0.05
    nM = round(nM, 2)
        
    nbP = nM / 0.01                     # Floor division does not work properly
                                        # in this case.

    return nbQ + nbD + nbN + nbP

positif = False
while not positif:
    try:
        montant = float(input('Entrez le montant en dollars: '))

        if montant < 0:
            print("Veuillez entrer une valeur numérique positive.")
        else:
            nbMin = piecesMin(montant)
            print("Le caissier aura besoin d'un minimum de {0:.0f}"\
                    " pièces.".format(nbMin))
            positif = True

    except ValueError:
        print("Veuillez entrer une valeur numérique.")
    except KeyboardInterrupt:
        print("\nAurevoir...")
        sys.exit()


