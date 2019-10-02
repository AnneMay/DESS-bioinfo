#! /usr/bin/python3

#Decription du programme pour l'usager
print("""
============================================
Détecteur de motifs dans une séquence d'ADN
Auteur: Anne-Marie Roy
Date: Automne 2019
============================================
""")

### Importations : Aucune

### Variables et validations
message_adn = "Veillez saisir une sequence d'ADN valide: "
message_motif = "Veuillez entre la longueur de motif désirée: "
#initialisation des variables
seq_adn = "0"
valMotif = -1

#Validation de l'input:
n = 0
while n < 3:
    len_adn = len(seq_adn)
    seq_count = seq_adn.count ("a") + seq_adn.count("g") + seq_adn.count("t") + seq_adn.count("c")
    if seq_count != len_adn:
        seq_adn = input(message_adn)
        seq_adn = seq_adn.lower()
    n += 1
if seq_count == len_adn:
	print("La séquence est valide.")
else:
    print("Fin impromptue du script. La sequence n'est pas valide.")
    quit()

#Validation de l'input - Motif:
n = 0
while n < 3:
    if valMotif <= 0 or valMotif > len_adn:
        valMotif = int(input(message_motif))
    n += 1
if valMotif > 0 and valMotif <= len_adn:
    print("La longueur de motif est valide.")
else:
    print("Fin impromptue du script. La longueur du motif n'est pas valide.")
    quit()

### Boucle de détection des motifs présents dans la séquence
n = valMotif #Utilisé pour copier puis manipuler la valeur associé au motif
fin = (len_adn - valMotif) + 1 # +1 pour inclure la valeur de (len_adn - valMotif)
ListMotif = list()
for i in range(0, fin):
    a = seq_adn[i:n]
    n += 1
### Boucle de validation de motif unique
    for j in range(0, len(ListMotif)):
        if a == ListMotif[j]:
            a = 0
### Ajout du motif unique à la liste
    if a != 0:
        ListMotif += [a]
###Compte de l'occurence de chacun des motifs
for i in range(0, len(ListMotif)):
    a = seq_adn.count(ListMotif[i])
    print(ListMotif[i], a)

###Indique la fin du script.
print("Fin du script")
