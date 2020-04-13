dataset=open('../dataset/rosalind_rna.txt')
DNA=''
RNA=''
for data in dataset:
    DNA = data
    for base in DNA:
        if(base == 'T'):
            RNA= RNA + 'U'
        else:
            RNA = RNA + base
    print(RNA)