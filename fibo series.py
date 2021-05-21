def fibo(n):
    n1=0
    print(n1,end=' ')
    n2=1
    print(n2,end=' ')
    for m in range(2,n):
        n3=n1+n2
        print(n3,end=' ')
        
        n1=n2
        
        n2=n3
fibo(10) 


print('-'*70)


def fibo(n):
    n1=0
    n2=1
    for i in range(n):
        n3=n1+n2
        print(n1,end=' ')
        n1=n2
        n2=n3
fibo(8)        


