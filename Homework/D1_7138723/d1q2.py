#! /usr/bin/env python3
################################################################################
#     File Name           :     d1q2.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-09-19 16:36]
#     Last Modified       :     [2015-09-19 23:06]
#     Description         :     Calcule le nombre minimal de pièce de monnaie 
#                               nécessaire pour une valeur en $ donnée.
################################################################################
import sys
positif = False
while not positif:
    try:
        montant = float(input('Entrez le montant en dollars: '))
    except ValueError:
        print("Veuillez entrer une valeur numérique.")
    except KeyboardInterrupt:
        print("\nAurevoir...")
        sys.exit()
    else:

        if montant < 0:
            print("Veuillez entrer une valeur numérique positive.")
        else:
            qMod = montant % 0.25
            nbQuarters = montant // 0.25

            nbDimes = qMod // 0.10
            dMod = round(qMod, 2) % 0.10    # round() est utilisé afin d'éviter
                                            # les cas où le modulo est 0.199 
                                            # où l'on obtiendrai 1 pièce 
                                            # de moins que la vraie réponse

            nbNickels = dMod // 0.05
            nMod = round(dMod, 2) % 0.05

            nbPennies = nMod // 0.01
            pMod = round(nMod, 2) % 0.01

            nbMin = nbQuarters + nbNickels + nbDimes + nbPennies
            print("Le nombre minimum de pièces est: {0:.0f}".format(nbMin))
            positif = True



