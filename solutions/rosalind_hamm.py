dataset=open('../dataset/rosalind_hamm.txt')
s=dataset.readline()
t=dataset.readline()

a=0
hamming=0

for base in s:
    if (base == 'A' or base == 'G' or base == 'C' or base == 'T' ):
        if (base != t[a]):
            hamming = hamming + 1
        a = a + 1

print(hamming)