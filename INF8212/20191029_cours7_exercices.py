#Exercices sur les fonctions
from random import randint
"""
def valider_entier(min, max, invite, erreur):
    choix = -1
    while not (min < choix < max):
        choix = int(input(invite + ":"))
        if not (min < choix < max):
            print(erreur)
    return choix

def divisible_4(entier):
    return entier % 4 == 0

def non_divisible_100(entier):
    return entier % 100 != 0

def divisible_400(entier):
    return entier % 400 == 0

def estBisextile(annee):
    return (divisible_4(annee) and non_divisible_100(annee)) or divisible_400(annee) #lecture plus claire qu'avec l'utilisation des opérateurs

def estBisextile2(annee):
    return ((annee % 4 == 0) and (annee % 100 != 0)) or (annee % 400 == 0)

annee = valider_entier(1900, 2050, "Saisir une année", "Votre année doit être comprise entre 1900 et 2050")

#Validation de la fonction
for i in range(10):
    annee = randint(1900, 2050)
    if estBisextile(annee):
        print(annee, "est bisextile")
    else:
        print(annee, "n'est pas bisextile")
"""
#Fonction qui prend en paramètre une liste d'entier et qui retourne
#le min le max la longeur et la somme
"""
def stat_entiers(entier):
    return min(entier), max(entier), len(entier), sum(entier)

liste_entiers = [24,35,67,95,82,83,10]
minimun, maximum, taille, somme = stat_entiers(liste_entiers)

print(minimun, maximum, taille, somme) # affiche les valeurs indépendemment
print(stat_entiers(liste_entiers)) #affiche le tuple
"""

def triangle(taille, type = "neutre"):
    if type == "neutre":
        
