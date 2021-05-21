#1.Write a program To put even and odd elements in a list into two different lists?

#sol:
'''
O/P:
[0, 2, 4, 6, 8]
[1, 3, 5, 7]
'''
#CODE:

l=[1,2,3,4,5,6,7,8,9]
l1=[]
l2=[]
for i in range(len(l)):
    if l[i]%2!=0:
        l1+=[i]
    else:
        l2+=[i]

print(l1)
print(l2)

print('-'*80)

#2.Write a program To Merge Two Lists and Sort it?

#sol:
'''
O/P:
I/P List= [2, 3, 5, 7, 9, 1, 4, 6, 8]
O/P List [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
#CODE:
l1=[2,3,5,7,9]
l2=[1,4,6,8]
l=l1+l2
print('I/P List=',l)
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]      
print('O/P List',l)

print('-'*80)

#3.Write a program To Sort the List According to the Second Element in Sublist?

#sol:
'''
O/P:
I/P List= [[1, 7, 5, 8], [2, 3, 5, 7], [6, 4, 3, 9]]
O/P List [[2, 3, 5, 7], [6, 4, 3, 9], [1, 7, 5, 8]]
'''

#CODE:
l=[[1,7,5,8],[2,3,5,7],[6,4,3,9]]
print('I/P List=',l)
for i in range(0,len(l)):
    for j in range(0,len(l)-i-1):
        if (l[j][1]>l[j+1][1]):
            res=l[j]
            l[j]=l[j+1]
            l[j+1]= res
print('O/P List',l)

print('-'*80)

#4.write a program To Swap the First and Last Value of a List?

#sol:
'''
O/P:
I/P List [3, 4, 8, 7, 5, 9, 6, 2]
O/P List= [2, 4, 8, 7, 5, 9, 6, 3]
'''

#CODE:
l=[3,4,8,7,5,9,6,2]
print('I/P List',l)

for i in range(len(l)):
    if l[0]>l[-1]:
        l[i],l[-(i+1)]=l[-(i+1)],l[i]
print('O/P List=',l)

print('-'*80)

#5.Write a Program To Remove the Duplicate Items from a List?

#sol:
'''
O/P:
I/P List=  [1, 6, 5, 2, 4, 3, 8, 7, 9, 2, 2, 3, 5, 2, 2]
O/P List=  [1, 6, 5, 2, 4, 3, 8, 7, 9]
'''
#CODE:
l=[1,6,5,2,4,3,8,7,9,2,2,3,5,2,2]
n_d=[]
print('I/P List= ',l)
for i in l:
    if i not in n_d:
        n_d+=[i]
print('O/P List= ',n_d)


print('-'*80)

#6.Writa a Program To Read a List of Words and Return the Length of the Longest One?

#sol:
'''
O/P:
Length of each Word is=  [2, 3, 5, 11]
Length of Longest Word is=  11
'''
#CODE:
l=['HI','BYE','HELLO','HELLO WORLD']
lenths=[]
for i in l:
    lenths+=[int(len(i))]

print('Length of each Word is= ',lenths)
print('Length of Longest Word is= ',max(lenths))

print('-'*80)

#7.Write a program To Remove the ith Occurrence of the Given Word in a List where Words can Repeat?

#sol:
'''
O/P:


#CODE:
a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input("Enter element" + str(x+1) + ":")
    a.append(element)
print(a)
c=[]
count=0
b=input("Enter word to remove: ")
n=int(input("Enter the occurrence to remove: "))
for i in a:
    if(i==b):
        count=count+1
        if(count!=n):
            c.append(i)
    else:
        c.append(i)
if(count==0):
    print("Item not found ")
else: 
    print("The number of repetitions is: ",count)
    print("Updated list is: ",c)
    print("The distinct elements are: ",set(a))
'''

print('-'*80)


#8.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')

#sol:
'''
O/P:

'''
#CODE:
p=int(input('enter the no of elements: '))
n=int(input('enter the elements: '))
l=[]
t=()
for i in n:
    l+=[i]
    t+=(i)
print(l)
print(t)




















        
