#! /usr/bin/env python3
###############################################################################
#     File Name           :     l7e4.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-11-03 11:59]
#     Last Modified       :     [2015-11-03 14:04]
#     Description         :     Exercice 4
###############################################################################


def move_zeros_v1(liste):
    tmp = []
    total_zero = 0

    for x in liste:
        if x == 0:
            total_zero += 1
        else:
            tmp.append(x)
    for i in range(1, total_zero+1):
        tmp.append(0)
    return tmp


def move_zeros_v2(liste):
    tmp = []
    total_zero = 0

    for x in liste:
        if x == 0:
            total_zero += 1
        else:
            tmp.append(x)
    for i in range(1, total_zero+1):
        tmp.append(0)
    del liste[0:len(liste)]
    liste.extend(tmp)


def move_zeros_v3(liste):
    nb = liste.count(0)
    lenL = len(liste)
    for x in range(0, nb):
        liste.append(0)
    for i in range(0, lenL):
        if liste[i] == 0:
            liste.remove(liste[i])


user_input = [int(i) for i in input().split(',')]
x = move_zeros_v1(user_input)
print(user_input, x)
y = move_zeros_v2(user_input)
print(user_input, y)
user_2 = [int(a) for a in input().split(',')]
z = move_zeros_v3(user_2)
print(user_2, z)
