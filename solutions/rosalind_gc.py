def gc(seq:str):
    c=seq.count('C')
    g=seq.count('G')
    n=0
    for l in seq:
        if (l == 'A' or l == 'T' or l == 'G' or l == 'C'):
            n = n+1
    print(n)
    return ((c + g)/n)*100

dataset=open('../dataset/rosalind_gc.txt')

fasta_line={}

idfasta=''
linefasta=[]
maxvalue=0
idmax=''
newline=''

for line in dataset:
    if(line.find('>')!= -1):
        linefasta=line.split('>')
        idfasta=linefasta[1]
        fasta_line[idfasta]=''
        newline=''
    else:
        newline=newline+line
        if (idfasta!= ''):
            fasta_line[idfasta] = gc(newline)
            if fasta_line[idfasta] > maxvalue:
                maxvalue=fasta_line[idfasta]
                idmax=idfasta


print(idmax)
newvalue=round(fasta_line[idmax], 6)
print(newvalue)





        