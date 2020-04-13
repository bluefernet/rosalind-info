def isSeqPalindromic(sequence: str):
    lenSequence = len(sequence)
    reverseSeq = ''
    while lenSequence >= 0:
        reverseSeq = reverseSeq + sequence[lenSequence:lenSequence + 1]
        lenSequence = lenSequence - 1
    i = 0
    while i < len(sequence):
        #print(sequence[i:i+1] + ' ' + reverseSeq[i:i+1])
        if (isReverseComplement(sequence[i:i+1], reverseSeq[i:i+1] )):
            i = i + 1
        else:
            return False
    return True

def isReverseComplement(seq1: str, seq2: str):
    if((seq1 == 'A' and seq2 == 'T') or (seq1 == 'T' and seq2 == 'A') ):
        return True
    else:
        if((seq1 == 'C' and seq2 == 'G') or (seq1 == 'G' and seq2 == 'C') ):
            return True
        else:
            return False

dataset = open('../dataset/rosalind_revp.txt')
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

for idFasta in fasta_line:
    #print('len: ' + str(len(fasta_line[idFasta])))
    k = 0
    while k + 4 < len(fasta_line[idFasta])+1:
        i = 4
        #print('!k! ' + str(k))
        while i <= 12:
            palindrom = fasta_line[idFasta][k:k+i]
            #print(palindrom)
            if((k+i) > len(fasta_line[idFasta])):
                #print('k: ' + str(k) + 'i: ' + str(i))
                #print('break ' + str(len(fasta_line[idFasta])) )
                break
            palindrom = fasta_line[idFasta][k:k+i]
            #print(palindrom + ': ' + str(k) + ' ' + str(i))
            if isSeqPalindromic(palindrom):
                print(str(k+1) + ' ' + str(i))
            i = i + 1
        k = k + 1
