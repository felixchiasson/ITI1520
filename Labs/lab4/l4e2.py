#! /usr/bin/env python3
###############################################################################
#     File Name           :     l4e2.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-06 11:35]
#     Last Modified       :     [2015-10-06 12:45]
#     Description         :     Print numbers from 1 to N  
###############################################################################
def bla(b):
    i = 1
    while i <= b:
        print(i,end=" ")
        i = i + 1
n = int(input("Veuillez entrer un numéro: "))
bla(n)
