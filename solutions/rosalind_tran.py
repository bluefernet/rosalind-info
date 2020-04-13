dataset = open('../dataset/rosalind_tran.txt')

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
        newline = ''
        fasta_line[idFasta] = ''
    else:
        newline = newline + line
        fasta_line[idFasta] = newline

print(fasta_line)

s = []
for dna in fasta_line:
    s.append(fasta_line[dna])

print(s)
transitions = 0
transversions = 0
i = 0
a = ''
b = ''
while i < len(s[0]):
    print(s[0][i:i+1])
    print(s[1][i:i+1])
    a = s[0][i:i+1]
    b = s[1][i:i+1]
    if (a == 'A' and b == 'G') or (a == 'C' and b == 'T') or (a == 'G' and b == 'A') or (a == 'T' and b == 'C'):
        print('transitions')
        transitions = transitions + 1
    else:
        if (a == 'A' and (b == 'C' or b == 'T')) or (a == 'C' and (b == 'A' or b == 'T')) or (a == 'T' and (b == 'C' or b == 'A')) or (a == 'G' and (b == 'C' or b == 'T')) or (a == 'C' and (b == 'G' or b == 'T')) or (a == 'T' and (b == 'C' or b == 'G')):
            print('transversions')
            transversions = transversions + 1
    i = i + 1

print(str(transitions) + ':' + str(transversions))
print(str(round((transitions/transversions),11)))
    
