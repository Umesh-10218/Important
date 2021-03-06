#DIAGONAL PATTERNS

#1)
#O/P:
'''
* * * * * * * 
*           * 
*           * 
*           * 
*           * 
*           * 
* * * * * * *
'''
#CODE:
n=7
for r in range(n):
    for c in range(n):
        if r==n-n or r==n-1 or c==n-n or c==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

print('-'*70)

#2)
#O/P:
'''
*           * 
  *       *   
    *   *     
      *       
    *   *     
  *       *   
*           *
'''
#CODE:
n=7
for r in range(n):
    for c in range(n):
        if r==c or r+c==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

print('-'*70)

#3)
#O/P:
'''
      *       
      *       
      *       
* * * * * * * 
      *       
      *       
      *
'''
#CODE:
n=7
if n%2==0:
    print('Not Possible to Print Required Pattern')

else:
    for r in range(n):
        for c in range(n):
            if r==n//2 or c==n//2:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
