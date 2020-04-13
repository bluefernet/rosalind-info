dataset = open('../dataset/rosalind_subs.txt')
s = dataset.readline()
t = dataset.readline()

lens = len(s)
lent = len(t)

i = 0
subs = ''

while i < lens:
    if(i + lent > lens ):
        break
    if (s[i:i+lent] == t):
        subs = subs + str(i+1) + ' '
    i = i + 1

print(subs)