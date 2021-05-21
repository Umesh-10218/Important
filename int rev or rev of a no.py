n=10218

def rev(n):
    res=0
    while n>0:
        ld=n%10
        res=res*10+ld
        n=n//10
    return res
ans=rev(10218)
print(ans)
    
    

     
     
