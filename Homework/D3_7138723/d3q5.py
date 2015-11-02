#! /usr/bin/env python3
###############################################################################
#     File Name           :     d3q5.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-28 14:38]
#     Last Modified       :     [2015-11-01 22:51]
#     Description         :     Count number of votes
###############################################################################

import sys


def vote_pourcentage(string):
    """

    (str) -> int
    Counts the total number of 'oui', 'abstention', and the total of words in
    a given string.
    Restrictions: string must contain at least one 'oui' or one 'non'.

    """

    total_yes = 0
    total_votes = 0
    total_abs = 0

    # Count all 'oui', 'abstention', and words.
    for i in string.split():
        total_votes += 1
        if i == 'oui':
            total_yes += 1
        elif i == 'abstention':
            total_abs += 1
        elif i == 'non':
            continue
        # Count anything other than 'oui' or 'non' as 'abstention'
        else:
            total_abs += 1

    return (total_yes / (total_votes - total_abs))*100

s = False

print("Entrez les votes (oui, non, abstention) séprarés par des "
      "espaces.")

while not s:
    try:
        vote_count = input()
        percentage_of_votes = vote_pourcentage(vote_count)

    # The function returns ZeroDivisionError if there are no 'oui' or 'non'
    # in the string.
    except ZeroDivisionError:
        print("Personne n'a voté. La motion ne passe pas.")
        s = True
    except KeyboardInterrupt:
        print('\n...Aurevoir!')
        sys.exit()

    else:
        if percentage_of_votes == 100:
            print('Unanimité')
        elif percentage_of_votes < 100 and percentage_of_votes >= ((2/3)*100):
            print('Majorité claire')
        elif percentage_of_votes < ((2/3)*100) and percentage_of_votes >= 50:
            print('Majorité simple')
        else:
            print('La motion ne passe pas')

        s = True
