from math import log10

dataset = open('../dataset/rosalind_prob.txt')

s = dataset.readline().rstrip('\n')
As = dataset.readline().split(' ')
A = []
B = []
i = 0
while i < len(As):
    A.insert(i, float(As[i]))
    B.insert(i, 0)
    i = i + 1

prob = 0
k = 0
for gcContent in A:
    prob = 0
    for base in s:
        print(gcContent)
        if base == 'A' or base == 'T':
            prob = prob + log10( ( 1 - gcContent  ) / 2 ) 
        else:
            prob = prob + log10( gcContent / 2 )
    B[k] = round(prob, 3)
    k = k + 1

output = ''
for log in B:
    output = output + str(log) + ' '
    
print(output)