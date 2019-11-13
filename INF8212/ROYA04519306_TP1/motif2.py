#! /usr/bin/python3
### Importations : Aucune
import sys
import os

#Decription du programme pour l'usager
print("""
============================================
Détecteur de motifs dans une séquence d'ADN
Auteur: Anne-Marie Roy
Date: Automne 2019
============================================
""")

###Fonctions
##Validation des arguments
def validation_arg(qte = 3, msg_usage = "script.py input output"):
    if len(sys.argv) != qte:
        print("Option illégale")
        print("Usage: ", msg_usage)
        sys.exit(-1)
#Validation saisies utilisateurs
def validation_essai_usager(nb_tentative, demande_usager, condition, repertoire):
    error = True
    n = 0
    while error and n < nb_tentative:
         val = input(demande_usager)
         #print(condition(val, repertoire))
         if condition(val,repertoire):
             error = False
         else:
             print("Entrée invalide")
             n += 1
    return error, val
#Valider des séquences d'ADN
def valider_adn(sequence, repertoire = ""):
    sequence = sequence.lower()
    return compte_atcg_seq(sequence) == len(sequence) and sequence != ""
#Compter les atcg dans une séquence
def compte_atcg_seq(sequence):
    compte = sequence.count("a")+sequence.count("t")+sequence.count("g")+sequence.count("c")
    return compte
#Valider l'index de suppression
def valider_idx(idx, repertoire = "sequence"):
    #print(len(repertoire))
    condition = idx != "" and int(idx) <= len(repertoire) and int(idx) > 0
    return condition
#Valider l'entier de choix
def valider_entier(entier, repertoire = ""):
    return entier != ""

##Charger les données d'un fichier
def ouvrir(file_chemin):
    if os.path.exists(file_chemin):
        file = open(file_chemin, "r")
        error = False
    else:
        file = []
        error = True
    return file, error
def charger_fichier(file_chemin):
    file, error = ouvrir(file_chemin)
    liste_elmt = []
    if not error:
        for each in file:
            each = each[0:len(each)-1]
            if valider_adn(each):
                liste_elmt += [each.lower()]
        file.close()
    return liste_elmt
##Imperssion à partir d'un dictionnaire
def impressionDict(dict, out = sys.stdout):
    for nom, valeur in dict.items():
        print(nom, valeur, file = out)

##Fonction associée aux choix du programme principal
def afficher_menu():
    print(#Menu de sélection
    """
    1- Ajouter une séquence
    2- Rechercher un motif dans les séquences
    3- Supprimer une séquence
    4- Sauvegarder et quitter le programme

    """
    )
#Affichage du Répertoire
def affichage(repertoire):
    print("Contenu du répertoire: ")
    for i in range(len(repertoire)):
        print("\t", i+1, end = "- ")
        print("\t", repertoire[i])
    print("\nFin du répertoire.")
#Ajouter des séquences d'ADN
def ajout(repertoire):
    error, seq = validation_essai_usager(3, "Votre séquence : ", valider_adn, repertoire)
    #print(seq)
    if not error:
        repertoire.append(seq.lower())
        print("séquence ajoutée")
    return repertoire
##Rechercher de motifs
def compte_motif(repertoire, motif):
    dict = {}
    for i in range(len(repertoire)):
        if motif in repertoire[i]:
            idx = "seq " + str(i+1) + " = "
            dict[idx] = repertoire[i].count(motif)
    return dict
def recherche(repertoire):
    error, motif = validation_essai_usager(3, "Votre séquence : ", valider_adn, repertoire)
    if not error:
        dict = compte_motif(repertoire, motif)
        impressionDict(dict)
        if not dict:
            print("le motif est absent des séquences de la DB")
    print("\nFin de la recherhce.")
##Suprimer des séquences
def suppression(repertoire):
    affichage(repertoire)
    error, idx = validation_essai_usager(3, "Entrer l'index désiré: ", valider_idx, repertoire)
    #print(error, idx)
    if not error:
        idx = int(idx) - 1 #Répertoire en base 1
        del repertoire[idx]
        print("La séquence avec l'index", idx+1, "a été supprimée.")
    else:
        print("index out of range")
    return repertoire
##Sauvegarder et Quitter
def sauver_quit(repertoire, output):
    print("Merci d'avoir utilisé ce programme")
    output = open(output, 'w')
    for each in range(len(repertoire)):
        print(repertoire[each], file = output)
    output.close()
    sys.exit(-1)

##Condition pour le programme principal
def condition_choix(choix, repertoire):
    if choix == "1": #Ajout de contact
        repertoire = ajout(repertoire)
        #print(repertoire)
    elif choix == "2": #Recherche
        recherche(repertoire)
    elif choix == "3": #Supression
        repertoire = suppression(repertoire)
    elif choix == "4": #Sortir
        # sauver_quit(repertoire, sys.argv[2])
        sauver_quit(repertoire, sys.argv[1])
    else:
        choix = 0
##Processus principal
def main():
    #validation_arg()
    validation_arg(2, "script.py  fichier.txt")
    sequence = charger_fichier(sys.argv[1])
    choix = 0
    while choix != "":
        afficher_menu()
        error, choix = validation_essai_usager(10, "Faites votre sélection : ", valider_entier, sequence)
        condition_choix(choix, sequence)

###Programme
if __name__ == "__main__":
    main()
