#! /usr/bin/env python3
###############################################################################
#     File Name           :     d2q3.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-11 10:56]
#     Last Modified       :     [2015-10-27 16:21]
#     Description         :     Outil d'apprentissage de multiplications et
#                               d'addition
###############################################################################
import sys
import operator
from random import randint


def jeuAM(c):
    """
    (int) -> (bool or int)
    Generates 10 random addition or multiplication problems based on the
    parameter.
    Restrictions: c must be 0 or 1

    """
    # Initialisation des variables locales

    operators = {"+": operator.add,     # Dictionnary used with the operator
                 "*": operator.mul}     # module. Saves us a few lines later on
    correct = 0

    # Choix de l'utilisateur

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
            print("Je n'ai pas bien compris votre choix. Veuillez choisir"
                  " l'option 0 ou 1. ")
            # Returns a boolean value (here: False). This will be used later on
            return choix

    # Jeu

    # Takes the value of 'op' as the key and returns the assigned function
    # (add() or mul()) and assigns it to typeOp.
    typeOp = operators[op]
    for i in range(0, 10):
        try:
            # Assign a random int value between 0 and 9 to a and b.
            a = randint(0, 9)
            b = randint(0, 9)

            print(a, op, b, '= ', end=' ')
            real = typeOp(a, b)
            reponse = int(input())

            if reponse == real:
                correct = correct + 1
            else:
                print("Incorrect - la réponse est", real)

        except ValueError:      # si la réponse n'est pas un chiffre
            print("Incorrect - la réponse est", real)
        except KeyboardInterrupt:
            print("\nDommage que vous partiez si tôt. Vous aviez", correct,
                  "bonne(s) réponse(s).")
            sys.exit()

    # If the program does not stop at the first else in the choosing section,
    # returns an int.
    return correct

# Main

# Initialize bonne as False and do not stop the loop until bonne is True
bonne = False

print("Ce logiciel va tester votre connaissance des opérations d'addition et "
      "de multiplication. \nVeuillez choisir entre 0) Addition et "
      "1) Multiplication (0 ou 1)")

while not bonne:
    # Run code and do something else if the program runs into a specified
    # exception

    try:
        choice = int(input())
        bonne = jeuAM(choice)

        if type(bonne) is bool:     # If bonne is a boolean
            continue                # try (loop) again (see jeuAM())
        elif bonne > 6:
            print(bonne, "réponses correctes. \nFélicitations!")
        else:
            print(bonne, "réponse(s) correcte(s). \nDemandez à votre "
                  "enseignant(e) pour vous aider.")
            break

    except ValueError:              # If user inputs non numerical value
        print("Vous avez entré un valeur qui n'est pas un chiffre. \nVeuillez "
              "faire votre choix (0 ou 1) à nouveau")
    except KeyboardInterrupt:       # If user exits with ^C
        print("\nAurevoir!")
        sys.exit()
