#! /usr/bin/env python3
###############################################################################
#     File Name           :     l2e1.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-09-22 11:36]
#     Last Modified       :     [2015-09-22 11:58]
#     Description         :     Affiche la division entière et le restant
#                               d'un input.
###############################################################################

nombr = int(input("Entrez le premier nombre: "))
nombre = int(input("Entrez le deuxième nombre: "))

divEn = nombr // nombre
modu = nombr % nombre

print("La division entière est", divEn, "et le reste est", modu)
