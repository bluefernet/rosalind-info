def fibo(n: int):
    if(n > 1):
        f1 = n - 1
        f2 = n - 2
        return (fibo(f1) + fibo(f2))
    if(n == 0):
        return 0
    if(n == 1):
        return 1

filei=open('../dataset/rosalind_fibo.txt')

for line in filei:
    a=int(line)
    fibonacci=fibo(a)
    print(fibonacci)