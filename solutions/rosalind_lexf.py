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

dataset = open('../dataset/rosalind_lexf.txt')

alphabet = dataset.readline().rstrip('\n').split(' ')
p = dataset.readline().rstrip('\n')
alphabet.sort()

# Disposizioni con ripetizine n^k es. n = 4 k = 2 --> 4^2 = 16

result = []
for l1 in alphabet:
    for l2 in alphabet:
        for l3 in alphabet:
            result.append(l1+l2+l3)

#print(result)
r = []
r = sorted(rDisp(alphabet, int(p)))
for a in r:
    print(a)
