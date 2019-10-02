#! usr/bin/python

"""
Tirage de loto 6 49
6 valeurs sans remise entre 0-49
"""
### Importations

import random

###Variables
List649 = list(range(1, (49+1), 1))
loto_gagnant = []

for i in range(6)
    position = randint(1,len(List649)-1)
    loto_gagnant.append(List649[position])
    del List649[position] #List649.remove(List649[position])
