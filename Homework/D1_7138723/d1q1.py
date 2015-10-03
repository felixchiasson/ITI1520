#! /usr/bin/env python3
################################################################################
#     File Name           :     d1q1.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-09-19 15:21]
#     Last Modified       :     [2015-10-03 09:49]
#     Description         :     Converts pounds and ounces to kilograms
################################################################################

# Import les libs nécessaires
import sys
positif = False 
while not positif: # Tant que positif est False
    try:
        pounds = float(input("Veuillez entrer le nombre de livres: "))
        ounces = float(input("Veuillez entrer le nombre d'onces: "))

        if pounds < 0 or ounces < 0:
            print("Votre valeur est négative. Veuillez entrer une valeur"\
                   " positive.")
        else:
            kilograms = pounds*0.453592 + ounces*0.0283495

            # On utilise .format() pour arrondir les valeurs
            print("{0:.1f} livres et {1:.1f} onces équivalent à {2:.4f} "\
                    "kilogrammes.".format(pounds, ounces, kilograms))
            
            positif = True

    # Dans le cas où float() ne peut pas convertir (si l'input != chiffre)
    except ValueError: 
        print("Vous n'avez pas entré une valeur numérique pour l'une des deux"\
                " options.")

    # Dans le cas où l'utilisateur arrête l'exécution avec ^C    
    except KeyboardInterrupt:
        print("\nAurevoir...")
        sys.exit() # Ferme sans erreur

        
