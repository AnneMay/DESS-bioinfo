TP 1 - Objectifs, Démarche et réflexion

BUT: d’indiquer le nombre de fois qu’apparait chaque motif (sous-séquence)
d’une taille donnée
pour une séquence biologique (ADN) valide.

sous-objectifs
1- Présenter le code à l'usager
2- Demander des valeurs à l'usager
    ***Faire la validation après chaque entrée de données
3- Valider les valeurs entrées par l'usager
    a) Seq ADN: Voir méthode premier cours et ajouter un if
    b) Nombre du motif: Voir cours 4 plusieurs exemples
    c) Arrêter le code si les données sont non valides à plus de 3 reprises,
      Voir cours 4, test fait par moi
4- Élaborer un processus qui permet de trouver toutes les combinaisons possible de motifs DANS LA SÉQUENCE fournie
    a) uiliser les index pour itérer dans la séquence et extraire les motifs.
    b) les stocker dans une liste pour ensuite itérer dans la liste
      PROBLÈME: Utilise la fonction append() qui ne fait pas partie des fonctions permises
    c) ? Doublons ?
5- Itérer sur chaque motifs et compter le nombre d'occurence
    a) ne pas présenter les motifs sans occurences

6- Annoncer la fin normale du script

Défis envisagés:
 - Algorithme de production de combinaisons
 - Multiple tabulation du au nombreuse loop et if imbriqué, voir si l'on peut
    essayer de les réduirent au maximum
 - Validation efficace et sans laisser de IF ouvert?

 Fonctions Autorisées
 Count() #Permet de compter les éléments d'une chaine ou d'une liste?
 print() #Permet d'afficher un résultats à l'écran
 items() #Permet d'afficher les items d'un dictionnaire
 int()  #permet de transformer une variable scalaire en nombre entier
 input() #permet de demander une information à l'usager
 upper() #Permet de transformer une chaine de caractère en majuscules
 lower() #Permet de transformer une chaine de caractère en minuscules
