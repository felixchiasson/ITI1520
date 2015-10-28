#! /usr/bin/env python3
################################################################################
#     File Name           :     l6e4.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-20 11:40]
#     Last Modified       :     [2015-10-20 13:46]
#     Description         :     Count with the count method
################################################################################
def compte(word, string):
    compteur = 0
    index = 0
    while index < (len(word)-len(string)+1):
        if string in word[index:index+len(string)]:
            compteur += 1

        index = index + 1
    return compteur
def compteB(c, s):
    return c.count(s)

word = input("Veuillez entrer le mot: ")

print(compte(word,'a'))
print(compte(word,'de la'))

print("Avec count()")
print(compteB(word,'a'))
print(compteB(word,'de la'))

