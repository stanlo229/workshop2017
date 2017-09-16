file = open("../rosalind_input/rna.txt","r")
dnafromfile = file.readline()
dna = dnafromfile.strip()

# dna = "GATGGAACTTGACTACGTAAATT"

rna = ""

#this for loop loops through every nucleotide
for nucleotide in dna:
	if nucleotide == "T":
		rna = rna + "U"
	else:
		rna = rna + nucleotide
	
print (rna)
