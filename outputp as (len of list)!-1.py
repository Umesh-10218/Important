def fact(n):
    out=1
    for i in range(n,1,-1):
        out*=i
    return out

l1=[10,21,8,57,76]
ans=fact(len(l1))
print(ans-1)
