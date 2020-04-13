dataset=open('../dataset/rosalind_prot.txt')
table = {}

table['UUU'] = 'F'      
table['CUU'] = 'L'      
table['AUU'] = 'I'      
table['GUU'] = 'V'
table['UUC'] = 'F'      
table['CUC'] = 'L'      
table['AUC'] = 'I'      
table['GUC'] = 'V'
table['UUA'] = 'L'      
table['CUA'] = 'L'      
table['AUA'] = 'I'      
table['GUA'] = 'V'
table['UUG'] = 'L'      
table['CUG'] = 'L'      
table['AUG'] = 'M'      
table['GUG'] = 'V'
table['UCU'] = 'S'      
table['CCU'] = 'P'      
table['ACU'] = 'T'      
table['GCU'] = 'A'
table['UCC'] = 'S'      
table['CCC'] = 'P'      
table['ACC'] = 'T'      
table['GCC'] = 'A'
table['UCA'] = 'S'      
table['CCA'] = 'P'      
table['ACA'] = 'T'      
table['GCA'] = 'A'
table['UCG'] = 'S'      
table['CCG'] = 'P'      
table['ACG'] = 'T'      
table['GCG'] = 'A'
table['UAU'] = 'Y'      
table['CAU'] = 'H'      
table['AAU'] = 'N'      
table['GAU'] = 'D'
table['UAC'] = 'Y'      
table['CAC'] = 'H'      
table['AAC'] = 'N'      
table['GAC'] = 'D'
table['UAA'] = 'stop'   
table['CAA'] = 'Q'      
table['AAA'] = 'K'      
table['GAA'] = 'E'
table['UAG'] = 'stop'   
table['CAG'] = 'Q'      
table['AAG'] = 'K'      
table['GAG'] = 'E'
table['UGU'] = 'C'      
table['CGU'] = 'R'      
table['AGU'] = 'S'      
table['GGU'] = 'G'
table['UGC'] = 'C'      
table['CGC'] = 'R'      
table['AGC'] = 'S'      
table['GGC'] = 'G'
table['UGA'] = 'stop'   
table['CGA'] = 'R'      
table['AGA'] = 'R'      
table['GGA'] = 'G'
table['UGG'] = 'W'      
table['CGG'] = 'R'      
table['AGG'] = 'R'      
table['GGG'] = 'G'

rna = dataset.readline()
rnalen = len(rna)

i = 0
prot=''
print(rna)
while i < rnalen-1:
    print(rna[i:i+3])
    decode = table[rna[i:i+3]]
    if(decode != 'stop'):
        prot= prot + decode
    i = i + 3

print(prot)

