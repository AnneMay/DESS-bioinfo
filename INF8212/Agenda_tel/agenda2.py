#! bin/bash/python3

###Introduction au programme
print(#Présentation du programme
"""
Agenda télephonique éphémère
Auteur: Anne-Marie Roy
Date: automne 2019
"""
)

###Package/import
#import csv

###Variables
choix = 0
carnet = []
###Fontions
##Menu
def afficher_menu():
    print(#Menu de sélection
    """
    1- Ajouter un contact
    2- Afficher le répertoire complet
    3- Rechercher un contact dans le répertoire
    4- Supprimer un contact
    5- Quitter le programme

    """
    )
##validation
def valider_entier(entier):
    while True: #validation de l'input
        try:
            entier = int(input("Faites votre sélection: "))
            break
        except ValueError:
            print("Oops!  Choisissez un nombre entre 1 et 5")
    
##Ajout
def ajout(agenda) :
    print("ajout")
    nom = input("Nom du contact: ")
    prenom = input("Prénom du contact: ")
    tel = input("Numéro de téléphone du contact: ")
    contact = {"nom":nom, "prenom":prenom, "num_tel":tel}
    agenda += [contact]
    print("Contact ", nom,", ", prenom, " ajouté.", sep = "")
##Affichage
def affichage(agenda):
    print("affichage")
    print("Contenu du répertoire: ")
    print("\tindex", "\tnom", "\tprénom", "\tnuméro_tel")
    for i in range(len(agenda)):
        print("\t", i+1, end = "- ")
        for key,value in agenda[i].items():
            print("\t", value, end = "; ")
        print("")
    print("\nFin du répertoire.")
##Recherhe
def recherche(agenda):
    print("Recherhe")
    motif = input("Recherche: ")
    for i in range(0, len(agenda)+1):
        for j in agenda[i]:
            if motif in agenda[i][j]:
                for key,value in agenda[i].items():
                    print(value, end = "; ")
        print("")
    print("\nFin de la recherhce.")
##suppression
def suppression(agenda):
    print("Supression")
    idx = int(input("Entrez l'index du contact à supprimer: ")) - 1 #Répertoire en base 1
    if idx < len(agenda) and idx >= 0:
        del agenda[idx]
        print("Le contact avec l'index :", idx+1, "a été supprimé.")
    else:
        print("La suppresion du contact a échoué, vérifiez l'index.")
        affichage(agenda)
##Quitter
def sauver_quit(agenda):
    print("Merci d'avoir utilisé ce programme")
    for i in range(len(agenda)):
        for key, val in agenda[i].items():
            print(val, file = "./agenda.txt")
    quit()

###Programme
while choix >= 0:
    afficher_menu()
    valider_entier(choix)
    if choix == 1: #Ajout de contact
        ajout(carnet)
    elif choix == 2: #Affichage du répertoire
        affichage(carnet)
    elif choix == 3: #Recherche
        recherche(carnet)
    elif choix == 4: #Supression
        suppression(carnet)
    elif choix == 5: #Sortir
        sauver_quit(carnet)
    else:
        print("Choisissez un nombre entre 1 et 5")
        choix = 0
