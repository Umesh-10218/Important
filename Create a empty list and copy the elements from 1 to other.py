l1=[12,61,78,62,35,48]
print(l1)

l2=[None]*len(l1)
print(l2)

for i in range(len(l1)):
    l2[i]=l1[i]
print(l2)
