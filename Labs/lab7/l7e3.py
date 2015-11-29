#! /usr/bin/env python3
###############################################################################
#     File Name           :     l7e3.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-11-03 11:48]
#     Last Modified       :     [2015-11-03 11:58]
#     Description         :     Exercice 3
##############################################################################

def somme_de_trois(x):

    for i in x:
        try:
            sum1 = x[i] + x[i+1] + x[i+2]
            sum2 = sum(x[i:i+2])
        except IndexError:
            return False
        else:
            if sum1 == 0:
                return True


t = (1,2,-3,4,-1,3)
t2 = (-3,4,1,2,-3)
t3 = (-2,-3,-4,-5,-6)

test_1 = somme_de_trois(t)
test_2 = somme_de_trois(t2)
test_3 = somme_de_trois(t3)
print("Avec le tuple (1, 2, -3, 4, -1, 3):", test_1)
print("Avec le tuple (-3, 4, 1, 2, -3):", test_2)
print("Avec le tuple (-2, -3, -4, -5, -6):", test_3)
