#! /usr/bin/env python3
###############################################################################
#     File Name           :     l4e3.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-06 11:43]
#     Last Modified       :     [2015-10-06 11:56]
#     Description         :     Asks user to guess randomly generated number 
###############################################################################
from random import randint

def devine(reponse):
    correct = False
    essai = 0
    print("Let's play a game! Devinez un nombre entre 1 et 10.")
    while not correct:
        reponse = int(input("Quel est le nombre? "))
        if reponse == r:
            print("Bravo! Vous avez réussi après", essai,"essai(s)")
            correct = True
        elif reponse != r and (reponse >= 1 and reponse <= 10):
            if reponse > r:
                print("Plus bas!")
            if reponse < r:
                print("Plus haut!")
            essai = essai + 1
        else:
            print("Veuillez entrer un chiffre entre 1 et 10!")
     
r = randint(1, 10)
devine(r)      

