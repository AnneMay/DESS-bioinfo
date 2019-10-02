"""
Exemple de validation
"""

MIN = 0
MAX = 1000
message_invite = "Saisir un nombre entre " + str(MIN) + " et " + str(MAX)
message_erreur = "Nombre invalide"
choix = (MIN-1)

while not (MIN < choix < MAX):
    choix = int(input(message_invite + " : "))
    if not (MIN < choix < MAX):
        print(message_erreur)
print("\nLenombre saisi est ", choix)

"""
Exemple de boucles
"""
maListe = [1,2,3,"allo", "le", "monde"]
for elt in maListe:
    print(elt, end=" ")

i = 0
while i < len(maListe):
    print(elt, end=" ")
    i = i + 1

print("Fin normale du script")
