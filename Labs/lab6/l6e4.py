#! /usr/bin/env python3
################################################################################
#     File Name           :     l6e4.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-20 11:40]
#     Last Modified       :     [2015-10-20 13:29]
#     Description         :     Count with the count method
################################################################################
def compte(c, s):
    compteur = 0
    index = 0
    while index < (len(c)-len(s)+1):
        if s in c[index:index+len(s)]:
            compteur += 1

        index = index + 1
    return compteur
def compteB(c, s):
    return c.count(s)

word = input("Veuillez entrer le mot: ")

print(compte(word,'a'))
print(compte(word,'de la'))

print("Avec count()")
print(word.compteB('a'))
print(word.compteB'de la'))

