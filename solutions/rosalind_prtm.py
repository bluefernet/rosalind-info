dataset = open('../dataset/rosalind_prtm.txt')

tableMassF = open('../dataset/monoisotopic_mass_table.txt')
isoMassTab = {}
for record in tableMassF:
    record = record.rstrip('\n')
    s = record.split(' ')
    isoMassTab[s[0]] = float(s[1])

prt = dataset.read().rstrip('\n')

totW = 0
for peptide in prt:
    print(peptide)
    totW = totW + isoMassTab[peptide]

print( round(totW, 3) )
