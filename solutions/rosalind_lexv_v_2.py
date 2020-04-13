# Problem: Ordering Strings of Varying Length Lexicographically
# Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n≤4).
# Return: All strings of length at most n formed from A, ordered lexicographically. (Note: alphabet order is based on the order in which the symbols are given.)

solution = []
def iteration(s: str, alphabet: list, n: int):
    if n > 0:
        for letter in alphabet:
            #print(s+letter)
            solution.append(s+letter)
            iteration(s+letter, alphabet, n-1)

dataset = open('../dataset/rosalind_lexv_test.txt')
output = open('rosalind_lexv_output_v_2.txt', 'w')
alphabet = dataset.readline().rstrip('\n').split(' ')
n = int(dataset.readline().rstrip('\n'))

iteration('', alphabet, n)

for word in solution:
    output.write(word+'\n')
