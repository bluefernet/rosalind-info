# Problem: Ordering Strings of Varying Length Lexicographically
# Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n≤4).
# Return: All strings of length at most n formed from A, ordered lexicographically. (Note: alphabet order is based on the order in which the symbols are given.)

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

# return true if s1 is less of s2, considering the weight indicating in the alphabet
def compare(s1: str, s2:str, d: dict):
    l1 = len(s1)
    l2 = len(s2)
    m = min(l1, l2)
    i = 0
    while i < m:
        if (s1[i:i+1] != s2[i:i+1]):
            if d[s1[i:i+1]] > d[s2[i:i+1]] :
                return True
            else:
                return False
        i = i + 1
    return False
    

def cocktailSort(a: list, key: dict): 
    n = len(a) 
    swapped = True
    start = 0
    end = n-1
    while (swapped == True): 
  
        # reset the swapped flag on entering the loop, 
        # because it might be true from a previous 
        # iteration. 
        swapped = False
  
        # loop from left to right same as the bubble 
        # sort 
        for i in range (start, end): 
            #if (a[i] > a[i + 1]) : 

            if (compare(a[i], a[i + 1], key)):

                a[i], a[i + 1]= a[i + 1], a[i] 
                swapped = True
  
        # if nothing moved, then array is sorted. 
        if (swapped == False): 
            break
  
        # otherwise, reset the swapped flag so that it 
        # can be used in the next stage 
        swapped = False
  
        # move the end point back by one, because 
        # item at the end is in its rightful spot 
        end = end-1
  
        # from right to left, doing the same 
        # comparison as in the previous stage 
        for i in range(end-1, start-1, -1): 
            #if (a[i] > a[i + 1]): 

            if (compare(a[i], a[i + 1], key)):

                a[i], a[i + 1] = a[i + 1], a[i] 
                swapped = True
  
        # increase the starting point, because 
        # the last stage would have moved the next 
        # smallest number to its rightful spot. 
        start = start + 1

dataset = open('../dataset/rosalind_lexv.txt')

alphabet = dataset.readline().rstrip('\n').split(' ')
n = int(dataset.readline().rstrip('\n'))
alphabetKey = {}

k = 1
for letter in alphabet:
    alphabetKey[letter] = k
    k = k + 1

print(n)
sol = []
i = 1
while i <= n:
    for element in rDisp(alphabet, i):
        sol.append(element)
    i = i + 1

#cocktailSort(sol, alphabetKey)
sol = sorted(sol)
cocktailSort(sol, alphabetKey)
output = open('rosalind_lexv_out.txt', 'w')
for tuples in sol:
    output.write(tuples+'\n')