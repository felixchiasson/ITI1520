#! /usr/bin/env python3
###############################################################################
#     File Name           :     l7e1.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-11-03 11:35]
#     Last Modified       :     [2015-11-03 11:41]
#     Description         :     Histogramme
###############################################################################

def triage(string):
    letters = {}

    for i in string:
        letters[i] = letters.get(i, 0) + 1

    return letters

string_input = input('Entrez une chaine de caractères: ')
string_tri = triage(string_input)
lettres_triees = list(string_tri.items())
lettres_triees.sort()
print(lettres_triees)

