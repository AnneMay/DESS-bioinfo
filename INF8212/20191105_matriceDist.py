#! usr/bin/python

##Packages
import sys

##fonctions
def validation_arg(qte = 3, msg_usage = "script.py input output"):
    if len(sys.argv) != qte:
        print("Option illégale")
        print("Usage: ", msg_usage)
        sys.exit(-1)
def extraire_metaDonnees(fichier):
    fh = open(fichier, "r")
    valeur1, valeur2 = fh.readline().split()
    fh.close()
    return int(valeur1), int(valeur2)
def extraire_ds_dict(fichier):
    dict = {}
    for each in fichier:
        elmt1, elmt2 = each.split()
        dict[elmt1] = elmt2
    return dict
def lectureAdict(fichier):
    fh = open(fichier, "r")
    #nb_seq, taille_seq = extraire_metaDonnees(fh)
    next(fh)
    dict = extraire_ds_dict(fh)
    fh.close()
    return dict
def impressionDict(dict, out = "std"):
    for nom, valeur in dict.items():
        print(nom, valeur, file = out) #Permet de ne garder qu'un seul saut de ligne à chacune des
def ecriture(fichier, contenu):
    fh = open(fichier, "w")
    impressionDict(contenu, fh)
    print("écriture terminée")

def seqToDist(a) :
    print ("ToDo")
    return
def sauvegarder_matrice_distances(outfile, seq, matrice) :
    fh = open(outfile, 'w')
    print(len(seq.keys()), len(list(seq.values())[0]), file = fh) #sauvegarde des fichiers 
    impressionDict(seq, fh)
    return


##Processus
validation_arg()
nb_seq, taille_seq = extraire_metaDonnees(sys.argv[1])
sequences = lectureAdict(sys.argv[1])
#ecriture(sys.argv[2], contenu)

matrice_distances = seqToDist(sequences)
sauvegarder_matrice_distances(sys.argv[2], sequences, matrice_distances)
