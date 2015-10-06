#! /usr/bin/env python3
###############################################################################
#     File Name           :     l4e4.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-06 11:57]
#     Last Modified       :     [2015-10-06 12:13]
#     Description         :     Calculateur de factoriel 
###############################################################################

def calculeFact(n):
    if n == 0:
        print("Le factoriel est 1")
    else:
        for i in range(1, n+1):
            i = i + 1
            reponse = i * i - 1
        print("Le factoriel est:", reponse)

positif = False
while not positif:
    number = int(input("Veuillez entrer un nombre entier positif: "))
    if number < 0:
        print("Veuillez entrer un nombre positif!")
    else: 
        calculeFact(number)
        positif = True
