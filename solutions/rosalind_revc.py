dataset=open('../dataset/rosalind_revc.txt')
c={}
a=0
DNA=''
for data in dataset:
    DNA=data
    print(DNA)
    for base in DNA:
        if(base == 'T'):
            c[a] = 'A'
        if(base == 'C'):
            c[a] = 'G'
        if(base == 'G'):
            c[a] = 'C'
        if(base == 'A'):
            c[a] = 'T'
        a=a+1
        print(c)


DNAc=''
a=a-1
while a > 0:
    a= a-1
    DNAc = DNAc + c[a]
    
print(DNAc)
