def fibo(n: int, k: int):
    if(n>1):
        f1 = n - 1
        f2 = n - 2
        return (fibo(f1, k)) + (fibo(f2, k) * k)
    if(n == 1):
        return 1
    if(n == 0):
        return 0

filei=open('../dataset/rosalind_fib.txt')

for line in filei:
    l=line.split(' ')
    num1=l.pop()
    num2=l.pop()
    k=int(num1)
    n=int(num2)
    rabbit=fibo(n, k)
    print(rabbit)