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
message_fin = "Fin impromptue du script. La sequence ou le motif ne sont pas valides."
#initialisation des variables
seq_adn = "0"
valMotif = -1
#Validation de l'input:
erreur = False
n = 0
while not erreur and n < 3:
    len_adn = len(seq_adn)
    seq_count = seq_adn.count ("a") + seq_adn.count("g") + seq_adn.count("t") + seq_adn.count("c")
    if n == 3: #3 essai (0, 1, 2), incrémentation en dehors de la condition
        erreur = True
    elif seq_count != len_adn:
            seq_adn = input(message_adn)
            seq_adn = seq_adn.lower()
    n += 1
if erreur:
    print(message_fin)
else:

#Validation de l'input - Motif:
    erreur = False
    n = 0
    while not erreur and n < 3:
        if n == 3: #3 essai (0, 1, 2), incrémentation en dehors de la condition
            erreur = True
        elif valMotif <= 0 or valMotif > len_adn:
            valMotif = int(input(message_motif))
        n += 1
    if erreur:
        print(message_fin)
    else:

###Boucle de détection des motifs
        dict = {}
        n = valMotif #Utilisé pour copier puis manipuler la valeur associé au motif
        fin = (len_adn - valMotif) + 1 # +1 pour inclure la valeur de (len_adn - valMotif)
        ListMotif = []
        for i in range(0, fin):
            a = seq_adn[i:n]
            n += 1
#Validation de motif unique et insertion dans le dictionnaire
            if a in dict:
                dict[a] += 1
            else:
                dict[a] = 1

###Affichage des résultats
        for cle,valeur in dict.items():
            print(cle, "=", valeur)

###Indique la fin du script.
        print("Fin du script")
