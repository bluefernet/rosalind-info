def fact(n: int):
    if n != 0:
        return n * fact(n-1)
    else: 
        return 1

def perm(s: list):
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
            for t in perm(copy):
                result.insert(x, str(n) + ' ' +str(t) )
                x = x + 1
        return result

def product(v1: list, v2: list):
    result = []
    for l1 in v1:
        for l2 in v2:
            result.append(l1+l2)
    return result

def rDisp(v: list, exp: int):
    result = []
    result = v
    while exp > 1:
        result = product(result, v)
        exp = exp - 1
    return result

def combine(v1: list, v2:list):
    result = []
    for l1 in v1:
        for l2 in v2:
            l3 = l2.split(' ')
            i = 0
            r = ''
            while i < len(l1):
                #print(l1[i:i+1] + l3[i])
                r = r + l1[i:i+1] + l3[i] + ' '
                i = i + 1
            r = r.rstrip('+')
            result.append(r)
    return result

dataset = open('../dataset/rosalind_sign.txt')

n = dataset.readline().rstrip('\n')

# B_n = 2^n * n! --> B_2 = 2^2 *2! = 8
v = []
i = 0
while i < int(n):
    v.append(str(i+1))
    i = i + 1

print(v)
permut = perm(v)
sign = [' ', '-']
disp = rDisp(sign, int(n))
print(disp)
print(permut)

print(combine(disp, permut))
print('result')
print(fact(int(n)) * 2**int(n))

resultFile = open('rosalind_sing_result.txt', 'w')
resultFile.write(str(fact(int(n)) * 2**int(n)) + '\n')
for comb in combine(disp, permut):
    print(comb.split(' '))
    for element in comb.split(' '):
        if(element != ''):
            resultFile.write(element + ' ')
    resultFile.write('\n')