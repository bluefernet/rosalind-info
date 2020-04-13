dataset=open('../dataset/rosalind_dna.txt')

for line in dataset:
    s=line

a=s.count('A')
c=s.count('C')
g=s.count('G')
t=s.count('T')
output = str(a) + ' ' + str(c) + ' ' + str(g) + ' ' + str(t)
print(output)
