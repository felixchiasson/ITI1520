#! /usr/bin/env python3
################################################################################
#     File Name           :     l6e3.py
#     Created By          :     Félix Chiasson (7138723)
#     Creation Date       :     [2015-10-20 12:03]
#     Last Modified       :     [2015-10-20 12:16]
#     Description         :     eh 
################################################################################

s = " En 1815, M. Charles-François-Bienvenu Myriel était évêque de Digne. C’était un vieillard d’environ soixante-quinze ans ; il occupait lesiège de Digne depuis 1806.  ... "

nS = s.replace(',',' ')
nS = nS.replace('.',' ')
nS = nS.replace(';',' ')
nS = nS.replace('\n',' ')
print(type(s), type(nS))
print("(A)",nS)
nS = nS.strip()
print("(B)",nS)
nS = nS.lower()
print("(C)",nS)
nb = nS.count('de')
print("(D)",nb)
nS = nS.replace('était','est')
print("(E)",nS)
