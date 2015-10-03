#! /usr/bin/env python3
################################################################################
#     File Name           :     d1q2.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-09-19 16:36]
#     Last Modified       :     [2015-10-03 10:20]
#     Description         :     Calcule le nombre minimal de pièce de monnaie 
#                               nécessaire pour une valeur en $ donnée.
################################################################################
import sys
positif = False
while not positif:
    try:
        montant = float(input('Entrez le montant en dollars: '))

        if montant < 0:
            print("Veuillez entrer une valeur numérique positive.")
        else:
            qMod = montant % 0.25
            qMod = round(qMod, 2)
            nbQuarters = montant // 0.25
            
            nbDimes = qMod // 0.10
            dMod = qMod % 0.10              # round() est utilisé afin d'éviter
                                            # les cas où le modulo est 0.199 
                                            # où l'on obtiendrais 1 pièce 
                                            # de moins que la vraie réponse
            dMod = round(dMod, 2)

            nbNickels = dMod // 0.05
            nMod = dMod % 0.05
            nMod = round(nMod, 2)
            
            nbPennies = nMod / 0.01         # Floor division does not seem to
                                            # work here. Using true division.
            pMod = round(nMod, 2) % 0.01

            nbMin = nbQuarters + nbNickels + nbDimes + nbPennies
            print("Le nombre minimum de pièces est: {0:.0f}".format(nbMin))

            positif = True


    except ValueError:
        print("Veuillez entrer une valeur numérique.")
    except KeyboardInterrupt:
        print("\nAurevoir...")
        sys.exit()



