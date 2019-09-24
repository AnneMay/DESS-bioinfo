#! bin/python
# ci-haut: chemin de l'interpréteur en bash
# Lecture d'une séquence au clavier
seq = input("votre séquence(minuscule): ") # utilise la fonction input de python qui lit une information au clavier
#Donc python affiche la string et attend le retour. Lorsque la séquence est entrée, la séquence est stocké dans la variable seq
# La variable seq est stockée dans la mémoire dynamique du programme.
# Mon idée serait de faire une boucle, mais l'enseignant propose une solution différente:
if seq.count ("a") + seq.count("g") + seq.count("t") + seq.count("c") != len(seq):
    print("La séquence n'est pas valide") #action si la condition est vraie
else: #Continue le code si la condition est fausse
    print("a = ", seq.count("a"))
    print("c = ", seq.count("c"))
    print("t = ", seq.count("t"))
    print("g = ", seq.count("g")) #La concaténation dans python est vraiment plus simple dans python vs R.
#donc on compte les occurences de chaque caractère et l'on la compare avec la longueur totale de la séquence
#Contrairement à l'itération, cette solution est plus optimale et prendra probablement moins de temps.
#Dans ce petit bout de de code on voit beaucoup de chose:
#La condition, l'appel de fonction, la comparaison, la synthaxe du if et les tabulations, l'input clavier et l'output écran.

#Langage de python n'a pas beaucoup d'élément qui sont réservés, probablement une des raisons de sa popularité
#"" vs ''; '' c'est invariable alors qu'on peut exécuter du code qui est dans un ""
