def lcm(n1,n2,n3):
    tl=n1
    if n2>n1 and n2>n3:
        tl=n2
    else:
        tl=n3
    mtl=tl
    while True:
        if(tl%n1==0 and tl%n2==0 and tl%n3==0):
            return tl
    tl+=mtl
ans=lcm(8,16,64)
print('Lcm is',ans)
