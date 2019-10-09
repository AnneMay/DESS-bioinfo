
"""
Boucle "for" va au suivant à chaque tour,
Boucle "while" on doit indiquer l'incrément de chacun des tours
exemple -->
"""
sequence = range(10, 20)

print("for") #ici le i est optionnel et ne sert qu'à l'affichage
i = 0
for elt in sequence: #elt = element
    print(i, elt, sep = "->")
    i += 1

print("while") #ici le i est essentiel
i = 0 # i = index
while i < len(sequence):
    print(i, sequence[i], sep = "->")
    i += 1

i = 0
while i < len(sequence): #s'assurer que l'on peut sortir de la boucle, pas de boucle infinie
    if i % 2 == 0:
        print("nombre pair")
        print(sequence[i])
        i += 1
    else:
        print(sequence[i])
        i +=2

"""
Exercice:
Écrire un script Python qui indique le nombre de fois qu’apparait
chaque entier d’une liste d’entiers saisie au clavier (une seule saisie).
"""

saisie = input("Entrez une série de nombre : ")
listEntier = []
for i in range(0, len(saisie)):
    a = saisie[i]
    for j in range(0, len(listEntier)):
        if a == listEntier[j]:
            a = 0
        elif a == " ":
            a = 0
    if a != 0:
        listEntier += [a]
for i in range(0, len(listEntier)):
    print(listEntier[i], saisie.count(listEntier[i]))

"""
Solution professeur
+
déterminer si une liste contient seulement des entiers
"""

# Validation
erreur = False
i = 0
while erreur == False and i < len(saisie):
    if "0" <= saisie[i] <= "9":
        n = 1
        i += 1
        print("nombre valide", saisie[i-1])
    elif saisie[i] == " ":
        i += 1
        print("C'est un séparateur")
    else:
        erreur = True
        print("ce n'est pas un nombre", saisie[i])
if erreur == True:
    quit()

#entiers = input("Mes entiers: ")
listeEntiers = saisie.split(" ")
dict = {}

for entier in listeEntiers:
    if entier in dict:
        dict[entier] += 1
    else:
        dict[entier] = 1
for cle,valeur in dict.items():
    print(cle, ":", valeur)
print(dict.items())


"""
Matrice et dictionnaire
"""
Mat = matrice[(1,2)]

for i in range(5):  #Jcomprend pas vraiment cet exemple à revoir
    for j in range(5):
        matrice[(i,j)] = 0
