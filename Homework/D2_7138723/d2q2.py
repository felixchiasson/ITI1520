#! /usr/bin/env python3
###############################################################################
#     File Name           :     l4e2.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-06 11:35]
#     Last Modified       :     [2015-10-14 12:21]
#     Description         :     Print numbers from a to b
###############################################################################
import sys

def printNb(a, b):
    "Prints numbers from a to b"
    while a <= b:
        print(a,end=" ")
        a = a + 1

s = False
while not s:
    try:
        n = int(input("Veuillez entrer le premier numéro: "))
        m = int(input("Veuillez entrer le deuxième numéro: "))
        if n > m:
            print("Votre premier chiffre est plus grand que le deuxième. Ce "
                    "programme compte en ordre croissant!")

        else:
            printNb(n, m)
            s = True

    except ValueError:      # Si l'utilisateur entre une lettre ou un symbol
        print("Veuillez entrer une valeur numérique")
    except KeyboardInterrupt:
        print("\n...Aurevoir!")
        sys.exit()
