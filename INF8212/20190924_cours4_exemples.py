#interpreteur

"""
Nom: Détecteur années bisextiles, exemple cours 4 
Auteur: Anne-Marie Roy
Date: 2019-09-24
"""

#Variable
annee = int(inptu("année à tester: "))

if ((annee % 4 == 0) and not (annee % 100 == 0)) or (annee % 400 == 0): #Utilisation des trois opérateurs logiques
    print(str(annee) + " est une année bisextile!")
else:
    print(str(annee) + " n'est pas une année bisextile!")

#Façon plus simple 1: mettre les tests de condition dans des variables
cond1 = (annee % 4 == 0) and not (annee % 100 == 0)
cond2 = (annee % 400 == 0)
isBis = cond1 or cond2 #Réduction du code pour le rendre encore plus lisible.

if isBis:
    print(str(annee) + " est une année bisextile!")
else:
    print(str(annee) + " n'est pas une année bisextile!")

#Façon encore plus optimale: mettre les conditions dans une seule fonction.



print("Fin normale du code")
