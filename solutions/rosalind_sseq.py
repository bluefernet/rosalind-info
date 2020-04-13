dataset = open('../dataset/rosalind_sseq.txt')

idFasta = ''
fasta_line = {}
newline = ''
idFastaS = []
cleanLine = ''
for line in dataset:
    if(line.find('\n') != -1):
        line = line.rstrip('\n')
    if(line.find('>') != -1):
        idFastaS = line.split('>')
        idFasta = idFastaS[1]
        newline = ''
        fasta_line[idFasta] = ''
    else:
        newline = newline + line
        fasta_line[idFasta] = newline

v = []
for data in fasta_line:
    v.append(fasta_line[data])    

s = v[0]
t = v[1]
lenT = len(t)

print(s)
print(t)
print(lenT)
i = 0
result = ''
k = 1

for base in s:
    #print(base)
    #print(t[i:i+1])
    if t[i:i+1] == base:
        result = result + str(k) + ' '
        i = i + 1
    k = k + 1

print('result ---> ' + result)