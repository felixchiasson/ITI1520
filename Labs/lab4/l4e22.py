#! /usr/bin/env python3
###############################################################################
#     File Name           :     l4e22.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-06 11:39]
#     Last Modified       :     [2015-10-06 11:42]
#     Description         :     Print 1 to N with a for loop 
###############################################################################

n = int(input("Entrez un numéro: "))
for i in range(1, n+1):
    print(i, end=" ")
    i = i + 1
