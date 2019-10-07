"""
Démonstration cours 5
Boucle de 1 à 100
Auteur: Anne-Marie Roy
"""
listA = []
for i in range(1,(100 + 1)):
    listA += [i]
print(listA)

somme = 0
for i in range(0, len(listA)):
    somme += listA[i]
print(somme)
print(sum(listA))

somme2 = []
for i in range(0, len(listA) - 1, 2): # -1 parce qu'on veut arrêter avant la dernière position
    n = listA[i] + (listA[i] + 1)
    somme2.append(n)
print(somme2)

"""
list1 = []
list2 = []
list3 = []
for x in range(1, 100, 2):
    list1.append(x)
for y in range(2, 101, 2):
    list2.append(y)
for z in range(0, 50):
    list3.append(list1[z] + list2[z])
print(list3)
"""
print("Fin du script")

"""
Peut utilisier des symboles de % avec le type de variable pour définir l'emplacement
d'une variable dans un print()
"""
age = 40
nom = "Anne"
var = (nom, age)
print("Je m'appelle", nom, "et j'ai", age, "ans")
print("Je m'appelle %s" % nom, "et j'ai %d ans" % age)
print("Je m'appelle %s et j'ai %d ans" % var)
