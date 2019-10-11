"""
Tuple = liste immuable. rien ne peux changer, on utilise des () pour les définir
on peut les utiliser comme clé dans un dictionnaire au contraire des listes

Exercice: clé = 1 à 100, valeur = nombre à la puissance 2
"""

dictEX = {}
for i in range(1,100+1):
    dictEX[i] = i**2
print(dictEX)

dict = {}
for i in range(1, 100+1):
    dict[i] = [(i**2),(i**3)]
print(dict)
