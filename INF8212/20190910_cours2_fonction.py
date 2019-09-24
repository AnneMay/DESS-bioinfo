#! bin/python

# nombre à convertir de décimale vers le reste
nbrdec1 = int(input("nombre décimal: "))

#Fonctions de conversion de nombre
#Fonction 1 Décimale vers binaire

def dec_to_bin(nombre1):
    listA = list() # crée une liste pour stoker les valeurs binaires
    while nombre1 > 0: #boucle pour évaluer le modulo du nombre puis le diviser par 2
        a = nombre1 % 2 #calcule le symbole binaire (le reste de la division)
        listA.insert(0, a) #Insère le symbole au début de la liste
        nombre1 = nombre1//2 #Divise le nombre par 2 et renvoie l'entier inférieur
    while len(listA) < 8:
        listA.insert(0, 0)
    print("binaire = ", *listA, sep = "") #Montre la listA à l'écran, devra probablement la formatter
    return
dec_to_bin(nbrdec1)

#La définition de la fonction octale se fait avec le même type de code, on remplace 2 par 8
def dec_to_oct(nombre1):
    listA = list() # crée une liste pour stoker les valeurs binaires
    while nombre1 > 0: #boucle pour évaluer le modulo du nombre puis le diviser par 2
        a = nombre1 % 8 #calcule le symbole binaire (le reste de la division)
        listA.insert(0, a) #Insère le symbole au début de la liste
        nombre1 = nombre1//8 #Divise le nombre par 2 et renvoie l'entier inférieur
    print("octale = ", *listA, sep = "") #Montre la listA à l'écran, devra probablement la formatter
    return
dec_to_oct(nbrdec1)

#La définition de la fonction hexadecimale se fait avec le même type de code, on remplace 2 par 16, on assigne 10-16
def dec_to_hex(nombre1):
    listA = list() # crée une liste pour stoker les valeurs binaires
    while nombre1 > 0: #boucle pour évaluer le modulo du nombre puis le diviser par 2
        a = nombre1 % 16 #calcule le symbole binaire (le reste de la division)
        digits = "0123456789ABCDEF"#Transforme a en 0 à F
        listA.insert(0, digits[a]) #Insère le symbole au début de la liste
        nombre1 = nombre1//16 #Divise le nombre par 2 et renvoie l'entier inférieur
    print("hexadecimale = ", *listA, sep = "") #Montre la listA à l'écran, devra probablement la formatter
    return
dec_to_hex(nbrdec1)

#Input d'un nombre binaire
#nbrbin = input("nombre binaire: ")

#Défition de binaire à Décimale
def bin_to_dec(nombre1):
    nbr = [int(digit) for digit in str(nombre1)]
    nbr.reverse()
    a = 0
    i = 0
    while (i < len(nbr)):
        a = a + (nbr[i]*(2**i))
        i = i + 1
    print("decimale = ", a, sep = "")

#bin_to_dec(nbrbin)

def bin_to_oct(nombre1):
    nbr = [int(digit) for digit in str(nombre1)]
    while (len(nbr) % 3) != 0:
        nbr.insert(0, 0)
    nbr.reverse()
    a = 0
    listA = list()
    i = 0
    while (i < len(nbr)):
        a = (nbr[i]*(2**0)) + (nbr[i+1]*(2**(1))) + (nbr[i+2]*(2**(2)))
        listA.insert(0, a)
        i = i + 3
    print("octale = ", *listA, sep = "") #Montre la listA à l'écran, devra probablement la formatter
    return

#bin_to_oct(nbrbin)

def bin_to_hexa(nombre1):
    nbr = [int(digit) for digit in str(nombre1)]
    while (len(nbr) % 4) != 0:
        nbr.insert(0, 0)
    nbr.reverse()
    a = 0
    listA = list()
    i = 0
    while (i < len(nbr)):
        a = (nbr[i]*(2**0)) + (nbr[i+1]*(2**(1))) + (nbr[i+2]*(2**(2))) + (nbr[i+3]*(2**(3)))
        digits = "0123456789ABCDEF"#Transforme a en 0 à F
        listA.insert(0, digits[a]) #Insère le symbole au début de la liste
        i = i + 4
    print("hexadecimale = ", *listA, sep = "") #Montre la listA à l'écran, devra probablement la formatter
    return

#bin_to_hexa(nbrbin)

nbroct = int(input("valeur octale: "))

def oct_to_dec(nombre1):
    nbr = [int(digit) for digit in str(nombre1)]
    nbr.reverse()
    a = 0
    i = 0
    while (i < len(nbr)):
        a = a + (nbr[i]*(8**i))
        i = i + 1
    print("decimale = ", a, sep = "")

oct_to_dec(nbroct)

def oct_to_bin(nombre1):
    nbr = [int(digit) for digit in str(nombre1)]
    listA = list() # crée une liste pour stoker les valeurs binaires
    for i in range(0, len(nbr)):
        while nbr[i] > 0: #boucle pour évaluer le modulo du nombre puis le diviser par 2
            a = nbr[i] % 2 #calcule le symbole binaire (le reste de la division)
            listA.insert(0, a) #Insère le symbole au début de la liste
            nbr[i] = nbr[i]//2 #Divise le nombre par 2 et renvoie l'entier inférieur
        while len(listA) < 3:#ajouter avant pour que chaque nombre ait 3 bites
            listA.insert(0, 0)
    while len(listA) < 8:
        listA.insert(0, 0)
    print("binaire = ", *listA, sep = "") #Montre la listA à l'écran, devra probablement la formatter
    return

oct_to_bin(nbroct)

def oct_to_hexa(nombre1):
    nbr = [int(digit) for digit in str(nombre1)]
    listA = list() # crée une liste pour stoker les valeurs hexadecimale
    listB = list()
    a = 0
    i = 0
    while (i < (len(nbr))):
        a = ((nbr[i])*(8**(i)))
        listB.insert(0, a)
        nbr2 = sum(listB)
        i = i + 1
    while nbr2 > 0: #boucle pour évaluer le modulo du nombre puis le diviser par 2
        a = nbr2 % 16 #calcule le symbole binaire (le reste de la division)
        digits = "0123456789ABCDEF"#Transforme a en 0 à F
        listA.insert(0, digits[a]) #Insère le symbole au début de la liste
        nbr2 = nbr2//16 #Divise le nombre par 2 et renvoie l'entier inférieur
    print("hexadecimale = ", *listA, sep = "") #Montre la listA à l'écran, devra probablement la formatter
    return

oct_to_hexa(nbroct)

"""
Manque les fonctions pour tranformer les octales et les hexadecimales
"""
