dataset = open('../dataset/rosalind_lcsm.txt')


# ToDo da inserire in una funzione da importare nei vari programmi
# --- readFastaLine ---
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
        print(idFasta)    
        newline = ''
        fasta_line[idFasta] = ''
    else:
        newline = newline + line
        fasta_line[idFasta] = newline
    
print(fasta_line)

idMax = min(fasta_line)
maxC = len(fasta_line[idMax])
maxS = fasta_line[idMax]
i = 2

print(idMax)
print(maxC)
print(maxS)
result = 0
maxMotif = ''

while i < maxC:
    k = 0
    while k < maxC:
        if (k+i <= maxC):
            #print(maxS[k:k+i])
            motif = maxS[k:k+i]
            result = 0
            for idF in fasta_line:
                if fasta_line[idF].find(motif) == -1:
                    result = -1
                    break
            if result != -1:
                maxMotif = motif
        k = k + 1
    i = i + 1
        
print('')
print(maxMotif)
