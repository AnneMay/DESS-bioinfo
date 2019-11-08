#exemple de l'intra 2019

seq = input("Votre séquence: ")
motif = int(input("Votre taille de motif: "))

i = 0
n = motif

error = True

while error and i <= len(seq)-2*motif:
    if seq[i:n] == seq[i+motif:n+motif]:
        print("motif", seq[i:n], "en tandem")
        error = False
    i+=1
    n+=1

if error:
    print("pas de motif en tandem")

print("fin normale du script")
