dataset = open('../dataset/rosalind_cons.txt')

A = []
C = []
G = []
T = []
i = -1
lenline = 0
matrix = {}
longline = ''
for line in dataset:
    if (line.find('>') == -1):
        line = line.rstrip('\n')
        longline = longline + line
        matrix[i] = longline
    else:
        longline = ''
        i = i + 1
        if(lenline == 0):
            lenline = len(longline)

lenline = len(matrix[1])
print(lenline)
j = 0
while j < lenline:
    A.insert(j, 0)
    C.insert(j, 0)
    G.insert(j, 0)
    T.insert(j, 0)
    j = j + 1

num = 0
nucleotide = ''

while num < lenline:
    k = 0
    while k < len(matrix):
        dna = matrix[k]
        nucleotide = dna[num: num + 1]
        if(nucleotide == 'A'):
            A[num] = A[num] + 1
        if(nucleotide == 'C'):
            C[num] = C[num] + 1
        if(nucleotide == 'G'):
            G[num] = G[num] + 1
        if(nucleotide == 'T'):
            T[num] = T[num] + 1
        k = k + 1
    num = num + 1


n = 0
cons=''
while n < lenline:
    maxbase = max(A[n], C[n], G[n], T[n])
    if maxbase == A[n]:
        cons = cons + 'A'
    else:
        if maxbase == C[n]:
            cons = cons + 'C'
        else:
            if maxbase == G[n]:
                cons = cons + 'G'
            else:
                if maxbase == T[n]:
                    cons = cons + 'T'
    n = n + 1

print(cons)
tabA = 'A: '
for val in A:
    tabA = tabA + str(val) + ' '
print(tabA)

tabC = 'C: '
for val in C:
    tabC = tabC + str(val) + ' '
print(tabC)

tabG = 'G: '
for val in G:
    tabG = tabG + str(val) + ' '
print(tabG)

tabT = 'T: '
for val in T:
    tabT = tabT + str(val) + ' '
print(tabT)
