#! /usr/bin/env python3
################################################################################
#     File Name           :     d3q1.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-19 16:21]
#     Last Modified       :     [2015-10-19 16:58]
#     Description         :     Counts the number of positive values in a list
################################################################################
import sys

def countPos(L):
    """
    (list) -> int
    Counts the number of positive values in a list
    Restriction: L must be a list with numbers in it
    """
    counter = 0
    for i in L:
        if i > 0:
            counter += 1
        else:
            continue
    return counter

s = False

print("Veuillez entrer la liste de valeurs: ")

while not s:

    try:
# .split(',') removes commas and spaces between each elements of the list.
        liste = [int(x) for x in input().split(',')]
        positif = countPos(liste)
        print("Il y a", positif,"valeur(s) positive(s)")
        s = True

# Check for exceptions. ValueError happens when the user inputs letters instead
# of numbers.
# KeyboardInterrupt happens when the user tries to quit with ^C (makes quitting
# prettier by hiding the exception message entirely.
    except ValueError:
        print("Veuillez entrer au moins une valeur numérique.")
    except KeyboardInterrupt:
        print("\nAurevoir!")
        sys.exit()
