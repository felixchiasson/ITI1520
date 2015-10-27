#! /usr/bin/env python3
###############################################################################
#     File Name           :     d2q4.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-14 12:31]
#     Last Modified       :     [2015-10-27 16:23]
#     Description         :     Test l'utilisateur avec 10 problèmes
#                               arithmétiques aléatoirement distribués entre
#                               additions et multiplications.
###############################################################################
import sys

from random import randint


def randomOp(n):
    """

    (int) -> bool
    Generates an arithmetic problem with a given operator.
    Restrictions: n == 1 or 0

    """

    a = randint(0, 9)
    b = randint(0, 9)

    try:
        if n == 0:
            print(a, '+', b, '=', end=' ')      # End print statement with
            real = a + b                        # a white space to make the
            uAnswer = int(input())              # input fit on the same line.

            if uAnswer == real:
                return True
            else:
                print("Incorrect - la réponse est", real)
                return False
        else:
            print(a, '*', b, '=', end=' ')
            real = a * b
            uAnswer = int(input())

            if uAnswer == real:
                return True
            else:
                print("Incorrect - la réponse est", real)
                return False

    # Check for exceptions to avoid ugly error messages
    # If user input cannot be converted to int
    except ValueError:
        print("Incorrect - la réponse est", real)
    # If user force closes with ^C
    except KeyboardInterrupt:
        print("\nAurevoir!")
        sys.exit()


# Set the number of correct answers to 0

bonne = 0

print("Ce logiciel va vous demander de répondre à 10 questions d'additions et "
      "de multiplications...")

for i in range(0, 10):

    op = randint(0, 1)
    correct = randomOp(op)

    if correct is True:
        bonne += 1
    else:
        continue

print(bonne, "réponses correctes.")

if bonne > 6:
    print("Félicitations!")
else:
    print("Demandez à votre enseignant(e) pour de l'aide.")
