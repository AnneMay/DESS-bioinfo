agenda.py

Utilisation:
Ce programme sert à enregistrer et naviguer dans un répertoir de contact téléphonique.
L'utilisateur sera présenté avec 5 choix d'actions dès son entrée dans le programme
1- Ajouter un contact
2- Afficher le répertoire complet
3- Rechercher un contact dans le répertoire
4- Supprimer un contact
5- Quitter le programme


Démarche:
On fera d'abord un menu offrant tous les choix à l'utilsateur
Chaque bloc d'action sera travaillé individuellement
??Possibilité de fonctionnaliser toutes les actions??

0- Menu
Imprimer les otpion à l'utilisateur
Demander un choix à l'utilsateur
Construire une condition mulitple qui enclenche les actions selon le choix de l'utilisateur

1- Ajout
demander les trois inputs à l'utilisateur
_nom
_prénom
_téléphone
Insérer les input dans un dictionnaire
Insérer le dictionnaire dans une liste

2- Affichage
Faire une boucle qui génère des index associés avec les contacts

3- Recherche
demander un motif de Recherche à l'utilsateur
Rechercher le motif (voir TP1 - motif.py)

4- Supression
demander un index de contact
??offrir une sortie pour afficher le répertoire complet avec index??

5- Quitter
avec la fonction quit() inhérente à pyhton

**S'assurer que si la valeur saisie esten dehors des choix, on revient à la demande de choix.

Problème envisagé

retour au menu
  Imbriquer le tout dans une boucle while ?

Clarté du code
  Incorporer les services dans des fonctions

Sauvegarde des données
  En tsv avec module csv

Erreur texte
  Exception
