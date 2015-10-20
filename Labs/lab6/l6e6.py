#! /usr/bin/env python3
################################################################################
#     File Name           :     l6e6.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-20 13:15]
#     Last Modified       :     [2015-10-20 13:24]
#     Description         :     ehhhh 
################################################################################

def coder(L):
    mot = ''
    index = 0

    while index < len(L):
        try:
            mot = mot + L[index+1] + L[index]
            index += 2
        except IndexError:
            mot = mot + L[index]
            return mot
    return mot

bla = input("Veuillez entrer votre message: ")
print(coder(bla))
