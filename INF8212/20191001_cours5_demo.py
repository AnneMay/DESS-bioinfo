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

print("Fin du script")
