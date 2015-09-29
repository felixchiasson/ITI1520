#! /usr/bin/env python3
###############################################################################
#     File Name           :     l3e2.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-09-29 11:49]
#     Last Modified       :     [2015-09-29 12:06]
#     Description         :     Recommande l'activité selon la température 
###############################################################################

def whatDo(temp):
    if temp >= 80.0:
        activity = 1
    elif temp >= 60.0 and temp < 80.0:
        activity = 2
    elif temp >= 40.0 and temp < 60.0:
        activity = 3
    else:
        activity = 4
    return activity

temperature = int(input("Quel est la température? "))


act = whatDo(temperature)

if act == 1:
    print('Allez faire de la natation!')
elif act == 2:
    print('Allez jouer au soccer!')
elif act == 3:
    print('Allez faire du volleyball!')
elif act == 4:
    print('Allez faire du ski!')
else:
    print('Je ne sais pas quoi vous recommander!')


