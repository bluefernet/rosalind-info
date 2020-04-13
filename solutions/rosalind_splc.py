def transcription(s: str):
    table={}
    record = []
    prt = []
    dnaCodonTable = open('../dataset/dna_codon_table.txt')
    for line in dnaCodonTable:
        line = line.rstrip('\n')
        record = line.split(' ')
        table[record[0]] = record[1]

    startCodon = 'ATG'
    endCodon1 = 'TAG'
    endCodon2 = 'TGA'
    endCodon3 = 'TAA'

    i = 0
    aminoacids = ''
    translate = False
    protein = ''
    k = 0
    trans = {}
    while s.find(startCodon) != -1:
        index = s.find(startCodon)
        s = s[index+3:]
        trans[s]='' 

    for chain in trans:
        protein='M'
        #print(chain)
        i = 0
        while i < len(chain):
            amino = chain[i:i+3]
            if len(amino) == 3:
                translate = True
                #print(amino + ' -> ' + table[amino])
            else:
                translate = False
                if protein != '':
                    prt.append(protein)
                protein=''
                translate = False
            if amino == endCodon1 or amino == endCodon2 or amino == endCodon3:
                if protein != '':
                    prt.append(protein)
                protein=''
                translate = False
                break
            if translate:
                protein = protein + table[amino]
            i = i + 3
    
    return prt

dataset = open('../dataset/rosalind_splc.txt')

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

i = 0
dna = ''
introns = []
for s in fasta_line:
    print(fasta_line[s])
    if i == 0:
        dna = fasta_line[s]
    else:
        introns.append(fasta_line[s])
    i = i + 1

print(dna)
print(introns)
t = ''

for intron in introns:
    t = ''
    for sub in dna.split(intron):
        t = t + sub
    dna = t
    print('--- POST ---')
    print(dna)

print('!!!')
print(transcription(dna)[0])
print('!!!')