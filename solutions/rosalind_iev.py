dataset = open('../dataset/rosalind_iev.txt')

line = dataset.readline()

n = line.split(' ')

lenn = len(n)

genotype = {
    '1' : 1,    # AA-AA
    '2' : 1,    # AA-Aa
    '3' : 1,    # AA-aa
    '4' : 0.75, # Aa-Aa
    '5' : 0.5,  # Aa-aa
    '6' : 0     # aa-aa
}

i = 1

offspring = 0

for couple in n:
    offspring = offspring + ((genotype[str(i)] * float(couple)) * 2)
    i = i + 1

print(offspring)