
def lcm(a,b):
    tl=a
    if b>a:
        tl=b
    mtl=tl
    while True :
        if tl%a==0 and tl%b==0:
            return tl
        tl+=mtl
ans=lcm(30,45)
print('Lcm is',ans)
            


print('-'*60)




