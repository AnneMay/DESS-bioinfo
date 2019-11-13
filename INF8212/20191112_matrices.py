import sys

def creation_matrice(taille):
    matrice = [0] * taille #Création des lignes; 1ere dimension
    for i in range(taille):
        matrice[i] = [0]*taille
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            matrice[i][j]??
    return matrice
def afficher_matrice(matrice):
    print("# TODO: ")
def main():
    if len(sys.argv) != 2:
        print("usage:", sys.argv[0], "taille")
    else:
        matrice = creation_matrice(sys.argv[1])
        afficher_matrice(matrice)

if __name__ == "__main__":
    main()
