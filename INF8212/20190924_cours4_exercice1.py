#! interpréteur?

"""
Problème: Encadrer une chaine d'une taille x
donc ont doit connaitre la taille de la chaine
"""
# Variables
#chaine = input("Saisir une chaine : ")
#longueur = len(chaine)

#Résultats
#print("="*(longueur + 4) + "\n= " + chaine + " =\n" + ("="*(longueur + 4)))

print("Fin problème 1")

"""
Problème tester si une chaine est un palindrome

"""

#variables:

chaine = input("Saisir une chaine: ")

#Étape 1: retirer les majustcules et les espaces
##EXEMPLE: Never odd or enven
chaine_min = chaine.lower() #never odd or even
chaine_norm = chaine_min.replace(" ", "") #neveroddoreven

#Etape 2: Comparer la chaine et son inverse pour voir si elles sont équivalentes
#transformer la chaine en liste et  utiliser la fonction inv?
liste_ordre = list(chaine_norm) #[n,e,v,e,r,o,d,d,o,r,e,v,e,n]
liste_inv = liste_ordre[:]
liste_inv.reverse() #[n,e,v,e,r,o,d,d,o,r,e,v,e,n]
chaine_inv = "".join(liste_inv)
##Comme on ne peut pas comparer deux listes, on doit retransformer les listes en string.

if chaine_norm == chaine_inv:
    print("C'est un palindrome!")
else:
    print("Ce n'est pas un palindrome")
