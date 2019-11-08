import sys

##Lecture du premier fichier
def validation_arg(qte = 3, msg_usage = "script.py input output"):
    if len(sys.argv) != qte:
        print("Option illégale")
        print("Usage: ", msg_usage)
        sys.exit(-1)
def lecture(fichier):
    fh = open(fichier, "r")
    contenu = ""
    for each in fh:
        contenu += each # lit les sauts de ligne comme des caractères à part entière
        print(list)
    fh.close()
    return list
def ecriture(fichier, contenu):
    fh = open(fichier, "w")
    print(contenu, file = fh, end = "") #Permet de ne garder qu'un seul saut de ligne à chacune des
    fh.close()
    print("écriture terminée")

validation_arg(3)
#assignation des arguments à des variables
infile = sys.argv[1] #S'assurer qu'il existe pour pouvoir lire à l'intérieur
outfile = sys.argv[2] #S'assurer qu'il n'existe pas

contenu = lecture(infile)
ecriture(outfile, contenu)

print("fin du script")
