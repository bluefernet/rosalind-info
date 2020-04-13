fr=open('../dataset/rosalind_ini5.txt', 'r')
fw=open('../dataset/rosalind_ini5_output.txt', 'w')
a=0
for line in fr:
    a=a+1
    if(a%2 == 0):
        fw.write(line)