chaine=input("chaine: ")
motif=input("motif: ")
resultat={}

if motif in chaine:
	resultat[motif]=chaine.count(motif)
print("option 1", resultat)

resultat={}
for i in range(len(chaine)):
	if motif == chaine[i:i+len(motif)]:
		if motif in resultat:
			resultat[motif] += 1
		else:
			resultat[motif] = 1
print("option 2", resultat)
