#! /usr/bin/env python3
###############################################################################
#     File Name           :     l2e2.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-09-22 11:58]
#     Last Modified       :     [2015-09-22 12:26]
#     Description         :     Fonction qui converti de Celcius à Faahrenheit 
###############################################################################

def celcius_to_F(c):                # Permet de convertir une valeur en celcius 
    f = c * 9.0/5.0 + 32            # en Fahrenhei t
    return f

t_C_global = float(input("Veuillez entrer  une valeur en Celcius: "))
print("La valeur en Fahrenheit est", celcius_to_F(t_C_global))

