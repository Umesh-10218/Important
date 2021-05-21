def isprime(n):
    flag=0
    if n==1:
        print('neither prime nor composite')
    for i in range (2,(n//2)+1):
        if n%i==0:
            flag=1
            break
        else:
            if n%i==0:
                flag=1
                break
    if flag==0:
        print('prime number')
    else:
        print('not a prime number')
print(isprime(18))










print('-'*60)



