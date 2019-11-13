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
    #next(fh)
    dict = extraire_ds_dict(fh)
    fh.close()
    return dict
def impressionDict(dict, out = sys.stdout):
    for nom, valeur in dict.items():
        print(nom, valeur, file = out) #Permet de ne garder qu'un seul saut de ligne à chacune des
def ecriture(fichier, contenu):
    fh = open(fichier, "w")
    impressionDict(contenu, fh)
    print("écriture terminée")
def creation_matrice(ligne, colonne):
    matrice = [0] * ligne #Création des lignes; 1ere dimension
    for i in range(ligne):
        matrice[i] = [0]*colonne
    return matrice
def initialisation_leveinstein(taille1, taille2, matrice):
    for i in range(taille1):
        matrice[i][0] = i
    for j in range(taille2):
        matrice[0][j] = j
    return matrice
def leveinstein(chaine1, chaine2):
    taille_c1 = len(chaine1) + 1
    taille_c2 = len(chaine2) + 1
    d = creation_matrice(taille_c1, taille_c2)
    d = initialisation_leveinstein(taille_c1, taille_c2, d)
    for i in range(1, taille_c1):
        for j in range(1, taille_c2):
            if chaine1.lower()[i-1] == chaine2.lower()[j-1]:
                cout = 0
            else:
                cout = 1
            d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + cout)
        #print(d)
    return d[len(chaine1)][len(chaine2)]
def seqToDist(sequence, file) : #distance de levenstein (vu avec Virginie dans les alignements)
    fh = open(file, "w")
    matrice = {} #matrice en dictionnaire
    for seq1 in sequence.values():
        for seq2 in sequence.values():
            #print(seq1, seq2)
            if seq1 == seq2:
                matrice[(seq1, seq2)] = leveinstein(seq1, seq2) #permet d'éviter les doublons
            else:
                if (seq1,seq2) in matrice.keys() or (seq2, seq1) in matrice.keys():
                    pass
                else:
                    matrice[(seq1, seq2)] = leveinstein(seq1, seq2) #permet d'éviter les doublons
            # print(seq1, seq2, file = fh)
            # print(leveinstein(seq1,seq2), file = fh)
    fh.close()
    return matrice
def sauvegarder_matrice_distances(outfile, seq, matrice) :
    fh = open(outfile, 'w')
    #print(len(seq.keys()), len(list(seq.values())[0]), file = fh) #sauvegarde des fichiers
    impressionDict(matrice, fh)
    return


##Processus
def main():
    validation_arg()
    #nb_seq, taille_seq = extraire_metaDonnees(sys.argv[1])
    sequences = lectureAdict(sys.argv[1])
    #ecriture(sys.argv[2], contenu)
    matrice_distances = seqToDist(sequences, sys.argv[2])
    #print(matrice_distances)
    sauvegarder_matrice_distances(sys.argv[2], sequences, matrice_distances)

if __name__ == '__main__':
    main()
