#TRIANGLE PATTERNS

#1)
#O/P:
'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * *
'''
#CODE:
n=7
for r in range(n):
    for c in range(n):                              
        if r>=c:
            print('*',end=' ')
    print()
        
print('-'*70)

#2)
#O/P:
'''
* * * * * * * 
  * * * * * * 
    * * * * * 
      * * * * 
        * * * 
          * * 
            * 
'''
#CODE:         
n=7
for r in range(n):
    for c in range(n):
        if r<=c:
            print('*',end=' ')
        else :
            print(' ',end=' ')
    print()
            
print('-'*70)

#3)
#O/P:
'''
* * * * * * * 
* * * * * *   
* * * * *     
* * * *       
* * *         
* *           
*       
'''
#CODE:
n=7
for r in range(n):
    for c in range(n):
        if r+c<=n-1:
            print('*',end=' ')
        else :
             print(' ',end=' ')
    print()
    
print('-'*70)

#4)
#O/P:
'''
            * 
          * * 
        * * * 
      * * * * 
    * * * * * 
  * * * * * * 
* * * * * * *
'''
#CODE:
n=7
for r in range(n):
    for c in range(n):
        if r+c>=n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

print('-'*70)

#5)
#O/P:
'''
1             
8 9           
15 16 17         
22 23 24 25       
29 30 31 32 33     
36 37 38 39 40 41   
43 44 45 46 47 48 49
'''
#CODE:
n=7
i=1
for r in range(n):
    for c in range(n):
        if r>=c:
            print(i,end=' ')
            i+=1
        else:
            print(' ',end=' ')
            i+=1
    print()

print('-'*70)

#6)
#O/P:
'''
1 
3 2 
6 5 4 
10 9 8 7 
15 14 13 12 11
'''
#CODE:
n=5
count=1
tmp=2
for r in range(n):
    dis=count
    for c in range(r+1):
        print(dis,end=' ')
        dis-=1
    count=count+tmp
    tmp+=1
    print()

print('-'*70)    
    
#7)
#O/P:
'''
1 
3 2 
6 5 4 
10 9 8 7 
15 14 13 12 11
'''
#CODE:
n=5
count=1
tmp=2
for r in range(n):
    dis=count
    for c in range(r+1):
        print(dis,end=' ')
        dis-=1
    count=count+tmp+r
    print()

print('-'*70)   

#8)
#O/P:
'''
1 
2 6 
3 7 10 
4 8 11 13 
5 9 12 14 15
'''
#CODE:
n=5
for r in range(n):
    count=r+1
    for c in range(r+1):
        print(count,end=' ')
        count=count+(n-1-c)
    print()

print('-'*70)  


#9)
#O/P:

#CODE:





