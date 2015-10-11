#! /usr/bin/env python3
###############################################################################
#     File Name           :     d2q3.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-11 10:56]
#     Last Modified       :     [2015-10-11 11:58]
#     Description         :     Outil d'apprentissage de multiplications et
#                               d'addition
###############################################################################
import sys
import operator

from random import randint

def jeuAM(c):
    operators = {"+": operator.add,
                 "*": operator.mul}
    correct = 0
############# Choix de l'utilisateur #############
    choix = False
    while not choix:
        if c == 0:
            print("Vous avez choisi de faire des problèmes d'addition!")
            op = "+"
            choix = True
        elif c == 1:
            print("Vous avez choisi de faire des problème de multiplication!")
            op = "*"
            choix = True
        else:
            print("Je n'ai pas bien compris votre choix. Veuillez choisir entre" 
            " l'option 0 ou 1. ")
            return choix

############# Jeu #############
    typeOp = operators[op]

    for i in range(0, 10):
        a = randint(0, 9)
        b = randint(0, 9)

        print(a, op, b, '= ', end=' ')
        reponse = int(input())
        real = typeOp(a, b)

        if reponse == real:
            correct = correct + 1
        else:
            print("Incorrect - la réponse est", real)
    return correct

bonne = False
while not bonne:
    try:
        choice = int(input("0 = add, 1 = mult... "))
        bonne = jeuAM(choice)

        if type(bonne) is bool:
            continue
        elif bonne > 6:
            print(bonne, "réponses correctes. \nFélicitations!")
        else:
            print(bonne, "réponses correctes. \nDemandez à votre enseignant(e)" 
            " pour vous aider.")
            break

    except ValueError:
        print("Je n'ai pas bien compris votre choix...")
    except KeyboardInterrupt:
        print("\nAurevoir!")
        sys.exit()



