#! /usr/bin/env python3
###############################################################################
#     File Name           :     d3q5.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-28 14:38]
#     Last Modified       :     [2015-11-01 19:28]
#     Description         :     Count number of votes
###############################################################################

import sys


def vote_pourcentage(string):

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

while not s:
    try:
        print("Entrez les votes (oui, non, abstention) séprarés par des "
              "espaces.")
        vote_count = input()
        percentage_of_votes = vote_pourcentage(vote_count)

        if percentage_of_votes == 100:
            print('Unanimité')
        elif percentage_of_votes < 100 and percentage_of_votes >= ((2/3)*100):
            print('Majorité claire')
        elif percentage_of_votes < ((2/3)*100) and percentage_of_votes >= 50:
            print('Majorité simple')
        else:
            print('La motion ne passe pas')
        s = True
    except ZeroDivisionError:
        print("Personne n'a voté. La motion ne passe pas.")
        s = True
    except KeyboardInterrupt:
        print('\n...Aurevoir!')
        sys.exit()
