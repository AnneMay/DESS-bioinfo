#! /usr/bin/python3
### Importations : Aucune
import sys

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
##validation
def valider_entier(entier):
    return True
##Validation saisies utilisateurs
def validation_essai_usager(nb_tentative, demande_usager, condition, repertoire):
    error = True
    n = 0
    while error and n < nb_tentative:
         val = input(demande_usager)
         if condition(val) and val != "":
             error = False
         else:
             print("Entrée invalide")
             n += 1
    return error, val
##Compter les atcg dans une séquence
def compte_atcg_seq(sequence):
    compte = sequence.count("a")+sequence.count("t")+sequence.count("g")+sequence.count("c")
    return compte
##Valider des séquences d'ADN
def valider_adn(sequence):
    sequence = sequence.lower()
    return compte_atcg_seq(sequence) == len(sequence)
##Condition de l'index de suppression
def valider_idx(idx, repertoire = "repertoire"):
    condition = idx != "" and int(idx) <= len(repertoire) and int(idx) > 0
    return condition
##Imperssion à partir d'un dictionnaire
def impressionDict(dict, out = sys.stdout):
    for nom, valeur in dict.items():
        print(nom, valeur, file = out)
        if not dict:
            print("le motif est absent des séquences de la DB")
##Charger les données d'un fichier
def charger_fichier(file_chemin):
    file = open(file_chemin, "r")
    liste_elmt = []
    for each in file:
        each = each[0:len(each)-1]
        if valider_adn(each):
            liste_elmt += [each.lower()]
    file.close()
    return liste_elmt
##Menu
def afficher_menu():
    print(#Menu de sélection
    """
    1- Ajouter une séquence
    2- Rechercher un motif dans les séquences
    3- Supprimer une séquence
    4- Sauvegarder et quitter le programme

    """
    )
##Affichage du Répertoire
def affichage(repertoire):
    print("Contenu du répertoire: ")
    for i in range(len(repertoire)):
        print("\t", i+1, end = "- ")
        print("\t", repertoire[i])
    print("\nFin du répertoire.")
##Ajouter des séquences d'ADN
def ajout(repertoire):
    error, seq = validation_essai_usager(3, "Votre séquence : ", valider_adn, repertoire)
    print(seq)
    if not error:
        repertoire.append(seq.lower())
        print("séquence ajoutée")
##Détection des motifs
def compte_motif(repertoire, motif):
    dict = {}
    for i in range(len(repertoire)):
        if motif in repertoire[i]:
            dict[repertoire[i]] = repertoire[i].count(motif)
    return dict
##Rechercher de motifs
def recherche(repertoire):
    error, motif = validation_essai_usager(3, "Votre séquence : ", valider_adn, repertoire)
    if not error:
        dict = compte_motif(repertoire, motif)
        impressionDict(dict)
    print("\nFin de la recherhce.")
##Suprimer des séquences
def suppression(repertoire):
    affichage(repertoire)
    error, idx = validation_essai_usager(3, "Entrer l'index désiré: ", valider_idx, repertoire)
    if not error:
        idx = int(idx) - 1 #Répertoire en base 1
        del repertoire[idx]
        print("La séquence avec l'index", idx+1, "a été supprimée.")
##Sauvegarder et Quitter
def sauver_quit(repertoire, output):
    print("Merci d'avoir utilisé ce programme")
    output = open(output, 'w')
    for each in range(len(repertoire)):
        print(repertoire[each], file = output)
    output.close()
    sys.exit(-1)
##Condition pour le main
def condition_choix(choix, repertoire):
    if choix == "1": #Ajout de contact
        ajout(repertoire)
    elif choix == "2": #Recherche
        recherche(repertoire)
    elif choix == "3": #Supression
        suppression(repertoire)
    elif choix == "4": #Sortir
        sauver_quit(repertoire, sys.argv[2])
    else:
        choix = 0
##Processusprincipal
def main():
    validation_arg(3)
    sequence = charger_fichier(sys.argv[1])
    choix = 0
    while choix != "":
        afficher_menu()
        error, choix = validation_essai_usager(20, "Faites votre sélection : ", valider_entier, sequence)
        condition_choix(choix, sequence)

###Programme
if __name__ == "__main__":
    main()
