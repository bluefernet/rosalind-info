def reverse_complement(dna):
    lookup = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([lookup[c] for c in reversed(dna)])

def orf(s):

    table={}
    record = []
    prt = []
    dnaCodonTable = open('dna_codon_table.txt')
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
        print(chain)
        i = 0
        while i < len(chain):
            amino = chain[i:i+3]
            if len(amino) == 3:
                translate = True
                print(amino + ' -> ' + table[amino])
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

dataset = open('../dataset/rosalind_orf.txt')
s=''
for line in dataset:
    if line.find('>') == -1:
        s = s + line.rstrip('\n')


result = orf(s)
result2 = orf(reverse_complement(s))
print('result')
print '\n'.join(set(result + result2))
