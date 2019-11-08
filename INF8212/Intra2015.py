"""
#Exercice de chevauchement
print("""
#
""")
#variables
MIN = 6
seq1 = ""
seq2 = ""

#Focntions
def chevauchement(s1, s2):
    if s1[0:MIN] == s2[len(s2)-MIN:len(s2)]:
        pos_seq_chvm = (len(s2)-MIN, len(s2)+len(s1)-MIN, 0, len(s2))
    elif s1[len(s1)-MIN:len(s1)] == s2[0:MIN]:
        pos_seq_chvm = (0, len(s1), len(s1)-MIN, len(s2)+len(s1)-MIN)
    else:
        pos_seq_chvm = (-1,-1,-1,-1)
    return pos_seq_chvm

while not seq1 == "fin":
    seq1 = input("Votre sequence: ")
    if seq1 != "fin":
        seq2 = input("Votre 2e sequence: ")
        if seq2 != "fin":
            x = chevauchement(seq1, seq2)
            print(x)
        else:
            seq1 = "fin"
"""
n = int(input("nombre : "))
cond1 = ((n % 3 == 0) or (n % 5 == 0) or (n % 7 == 0) or (n % 9 == 0))
if (n % 2 == 0) and cond1:
    print("pair ")
elif not (n % 2 == 0) or not cond1:
    print("impair ")
else:
    print("premier")
print("Fin du script")
