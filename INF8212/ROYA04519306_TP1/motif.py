#! /usr/bin/python3

#Decription du programme pour l'usager
print("""
============================================
Détecteur de motifs dans une séquence d'ADN
Auteur: Anne-Marie Roy
Date: Automne 2019
============================================
""")

## Importations : Aucune

##Variables et validations
message_adn = "Veillez saisir une sequence d'ADN valide: "
message_motif = "Veuillez entre la longueur de motif désiré: "
#Séquence d'ADN
seq_adn = "0"
len_adn = len(seq_adn)
seq_count = seq_adn.count ("a") + seq_adn.count("g") + seq_adn.count("t") + seq_adn.count("c")
#Validation de l'input:
n = 0
while n < 3:
    if seq_count != len_adn:
        #print("La séquence n'est pas valide")
        seq_adn = input(message_adn)
        seq_adn = seq_adn.lower()
        len_adn = len(seq_adn)
    n += 1
if seq_count != len_adn:
	print("Fin impromptue du script. La sequence n'est pas valide.")
else:
    print("La séquence est valide.")

    #Longueur du motif:
    valMotif = int(input("Veuillez entre la longueur de motif désiré: "))
    #Validation de l'input:
    n = 1
    while n < 3:
        if valMotif < 0 or valMotif > len_adn:
            print("Nombre invalide. Entrez une valeur supérieure à 0 et inférieur à la longueur de la séquence.")
            valMotif = int(input("Veuillez entre la longueur de motif désiré: "))
        n += 1
    if valMotif < 0 or valMotif > len_adn:
        print("Fin impromptue du script. La longueur du motif n'est pas valide.")
    else:
        print("La longueur de motif est valide.")

        ### Boucle de détection des motifs présents dans la séquence
        i = 0
        n = valMotif
        ListMotif = list()
        #for i in range(0, ((len_adn - valMotif)+1)): #
        while i < ((len_adn - valMotif) + 1):
            a = seq_adn[i:n]
            i += 1
            n += 1

            ### Boucle de validation de motif unique
            j = 0
            #for j in range(0, len(ListMotif)): #
            while j < len(ListMotif):
                if a != ListMotif[j]:
                    j += 1
                else:
                    a = 0
            ### Ajout du motif unique à la liste
            if a != 0:
                ListMotif += [a]
        #print(ListMotif)
        ###Compte de l'occurence de chacun des motifs
        i = 0
        #for i in range(0, len(ListMotif)): #
        while i < len(ListMotif):
            a = seq_adn.count(ListMotif[i])
            print(ListMotif[i], a)
            i += 1

###Indique la fin absolue du script, s'affichera même en cas d'erreurs.
print("Fin du script")
