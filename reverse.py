dna = "AAAACCCGGT"
reverse = ""
for nu in dna:
	if nu == "A":
		reverse = reverse + "T"
	else:
		reverse = reverse + nu
	if nu == "C":
		reverse = reverse + "G"
	else:
		reverse = reverse + nu
	if nu == "T":
		reverse = reverse + "A"
	else:
		reverse = reverse + nu
	if nu == "G":
		reverse = reverse + "C"
	else:
		reverse = reverse + nu
		
reverse [::-1]