#! /usr/bin/python3

"""
Programme : Résolution d'équation de second degré
Auteur: Anne-Marie Roy
Date: Automne 2019
"""

###Importations
import math

###Variables
a = 0
b = 0
c = 0
delta = 0
##Saisie
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

###Résolution
delta = (b**2) - (4*a*c) #math.pow(b,2) #pour b au carré

if delta > 0 :
    print("x1 =", ((-b - math.sqrt(delta))/(2*a)))
    print("x2 =", ((-b + math.sqrt(delta))/(2*a)))
elif delta == 0 :
    print("x =", (-b/(2*a)))
else:
    print("Solution de résolution avec nombres complexes")

print("Fin du script")
