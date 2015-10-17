#! /usr/bin/env python3
###############################################################################
#     File Name           :     l4e2.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-06 11:35]
#     Last Modified       :     [2015-10-17 10:50]
#     Description         :     Print numbers from a to b
###############################################################################
import sys

def printNb(a, b):
    """

    (int, int) -> None
    Prints numbers from a to b
    Restrictions: a, b must be int, b > a

    """
    while a <= b:
        print(a,end=" ")
        a = a + 1

s = False

print("Ce programme va compter de n à m.")

while not s:
    try:
        n = int(input("Veuillez entrer la valeur de n: "))
        m = int(input("Veuillez entrer la valeur de m: "))

        # Check for n > m specifically to avoid returning nothing and allow user
        # to try again
        if n > m:
            print("Votre premier chiffre est plus grand que le deuxième. Ce "
                    "programme compte en ordre croissant!")

        else:
            printNb(n, m)
            s = True

    except ValueError:      # Si l'utilisateur entre une lettre ou un symbol
        print("Veuillez entrer une valeur numérique")
    except KeyboardInterrupt:       # If user quits with ^C
        print("\n...Aurevoir!")
        sys.exit()
