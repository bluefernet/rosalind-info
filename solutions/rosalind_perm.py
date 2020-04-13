def fact(n: int):
    if n != 0:
        return n * fact(n-1)
    else: 
        return 1

def fibo(s: list):
    result = []
    x = 0
    permutation = ''
    copy = []
    copy2 = []
    if len(s) == 1:
        return 1
    if len(s) == 2:
        x = 0
        for number in s:
            copy2 = s.copy()
            copy2.remove(number)
            z = copy2.pop()
            permutation =  str(number) + ' ' + str(z)
            result.insert(x, permutation)
            x = x + 1
        return result
    else:
        x = 0
        for n in s:
            copy = s.copy()
            copy.remove(n)
            for t in fibo(copy):
                result.insert(x, str(n) + ' ' +str(t) )
                x = x + 1
        return result

dataset = open('../dataset/rosalind_perm.txt')

perm = int(dataset.readline().rstrip('\n'))

s = []

i = 0
while i < perm:
    s.insert(i, i + 1) 
    i = i + 1

out = open('rosalind_perm_out.txt', 'w')
print(str(fact(perm)))
out.write(str(fact(perm)))
for n in fibo(s):
    print(n)
    out.writelines(str(n)+'\n')