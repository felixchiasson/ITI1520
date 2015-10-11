#! /usr/bin/env python3
###############################################################################
#     File Name           :     d2q3.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-11 10:56]
#     Last Modified       :     [2015-10-11 12:24]
#     Description         :     Outil d'apprentissage de multiplications et
#                               d'addition
###############################################################################
import sys
import operator

from random import randint

def jeuAM(c):

############# Initialisation des variables locales ###############
    
    operators = {"+": operator.add,     # Dictionnary used with the operator
                 "*": operator.mul}     # module. Saves us a few lines later on
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
            # Returns a boolean value (here: False). This will be used later on.
            return choix

############# Jeu #############
    typeOp = operators[op]          # Takes the value of "op" as the key and 
                                    # returns the assigned description (+ or *
                                    # operators). The operator module then
                                    # creates a function typeOp that returns
                                    # the specified operation.
    for i in range(0, 10):
        # Assign a random int value between 0 and 9 to a and b.
        a = randint(0, 9)
        b = randint(0, 9)

        print(a, op, b, '= ', end=' ')
        reponse = int(input())
        real = typeOp(a, b)

        if reponse == real:
            correct = correct + 1
        else:
            print("Incorrect - la réponse est", real)

    # If the program does not stop at the first else in the choosing section,
    # returns an int.
    return correct

##################### Main #########################

# Initialize bonne as False and do not stop the loop until bonne is True
bonne = False
while not bonne:
# Run code and do something else if the program runs into a specified exception
    try:  
        choice = int(input("0 = add, 1 = mult... "))
        bonne = jeuAM(choice)

        if type(bonne) is bool:     # If bonne is a boolean
            continue                # try (loop) again
        elif bonne > 6:
            print(bonne, "réponses correctes. \nFélicitations!")
        else:
            print(bonne, "réponses correctes. \nDemandez à votre enseignant(e)" 
            " pour vous aider.")
            break                   # Forces loop to stop. Otherwise when bonne
                                    # = 0, the program keeps looping.

    except ValueError:              # If user inputs non numerical value
        print("Je n'ai pas bien compris votre choix...")
    except KeyboardInterrupt:       # If user exits with ^C
        print("\nAurevoir!")
        sys.exit()



