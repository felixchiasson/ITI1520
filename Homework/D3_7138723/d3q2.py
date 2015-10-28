#! /usr/bin/env python3
###############################################################################
#     File Name           :     d3q2.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-19 16:49]
#     Last Modified       :     [2015-10-28 14:21]
#     Description         :     Returns a bolean if all elements of a list are
#                               positive.
###############################################################################
import sys


def count_pos(L):
    """
    (list) -> bool
    Counts the number of negative values in a list and returns True if all
    elements of L are positive.
    Restriction: L must be a list with numbers in it
    """
    counter = 0
    for i in L:
        if i <= 0:
            counter += 1
            print(i)
        else:
            continue
    if counter > 0:
        return False
    else:
        return True

s = False

print("Veuillez entrer une liste de valeurs séparée par des virgules: ")

while not s:
    try:
        # .split(',') splits each comma-separated input
        # The input is then converted into a list for use in countPos()
        liste = [int(x) for x in input().split(',')]
        positif = count_pos(liste)
        print(positif)
        s = True

    except ValueError:      # in case anything but a number is entered
        print("Veuillez entrer au moins une valeur numérique.")
    except KeyboardInterrupt:   # in case user quits with ^C (cleaner quit)
        print("\nAurevoir!")
        sys.exit()
