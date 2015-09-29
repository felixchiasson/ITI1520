#! /usr/bin/env python3
###############################################################################
#     File Name           :     l3e1.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-09-29 11:47]
#     Last Modified       :     [2015-09-29 11:49]
#     Description         :     Évalue l'âge entre 18 et 55 ans inclusivement 
###############################################################################

age = int(input('Quel est votre âge? : '))


if age >= 17 and age <= 55:
    print("Transaction acceptée")
else:
    print("Transaction refusée")
