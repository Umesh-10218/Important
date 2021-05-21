#SQUARE PROGRAMS:

#1)
#O/P:
'''
 *  *  *  *  * 
 *  *  *  *  * 
 *  *  *  *  * 
 *  *  *  *  * 
 *  *  *  *  *
'''
#CODE:
n=5
for i in range(n):
    print(' * '*n)
    
print('-'*70)

#2)
#O/P:
'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *
'''
#CODE:
n=5
for r in range(n):
    for c in range(n):
        print('*',end=' ')
    print()

print('-'*70)

#3)
#O/P:
'''
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 
21 22 23 24 25 
'''
#CODE:
n=5
count=1
for r in range(n):
    for c in range(n):
        print(count,end=' ')
        count+=1
    print()

print('-'*70)

#4)
#O/P:
'''
A B C D E 
F G H I J 
K L M N O 
P Q R S T 
U V W X Y
'''
#CODE:
n=5
count=65
for r in range(n):
    for c in range(n):
        print(chr(count),end=' ')
        count+=1
    print()

print('-'*70)

#5)
#O/P:
'''
4a b c d e 
f g h i j 
k l m n o 
p q r s t 
u v w x y
'''
#CODE:
n=5
count=97
for r in range(n):
    for c in range(n):
        print(chr(count),end=' ')
        count+=1
    print()

print('-'*70)

#6)
#O/P:
'''
Aa Bb Cc Dd Ee 
Ff Gg Hh Ii Jj 
Kk Ll Mm Nn Oo 
Pp Qq Rr Ss Tt 
Uu Vv Ww Xx Yy
'''
#CODE:
n=5
c1=65
c2=97
for r in range(n):
    for c in range(n):
        print(chr(c1)+chr(c2),end=' ')
        c1+=1
        c2+=1
    print()

print('-'*70)

#7)
#O/P:
'''
* * * * * * * 
* *   *   * * 
*   * * *   * 
* * * * * * * 
*   * * *   * 
* *   *   * * 
* * * * * * *
'''
#CODE:
n=7
for r in range (n):
    for c in range (n):
        if r==0 or r==n-1 or c==0 or c==n-1 or r==c or r+c==n-1 or r==n//2 or c==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

print('-'*70)

#8)
#O/P:
'''
1   2  3   4   5  6  7 
8   9     11     13  14 
15    17  18  19     21 
22 23 24  25  26 27  28 
29    31  32  33     35 
36 37     39     41  42 
43 44 45  46  47 48  49
'''
#CODE:
n=7
count=1
for r in range (n):
    for c in range (n):
        if r==0 or r==n-1 or c==0 or c==n-1 or r==c or r+c==n-1 or r==n//2 or c==n//2:
            print( count , end= ' ')
            count+=1
        else:
            print(' ' , end= ' ')
            count+=1
    print()
    
print('-'*70)

#9)
#O/P:
'''
* $ * $ * $ * 
$ * $ * $ * $ 
* $ * $ * $ * 
$ * $ * $ * $ 
* $ * $ * $ * 
$ * $ * $ * $ 
* $ * $ * $ *
'''
#CODE:
n=7
for r in range(n):
    for c in range(n):
        if (r+c)%2==0:
            print('*',end=' ')
        else:
            print('$',end=' ')
    print()
    
print('-'*70)

#10)
#O/P:
'''
$ * $ * $ * $ 
* $ * $ * $ * 
$ * $ * $ * $ 
* $ * $ * $ * 
$ * $ * $ * $ 
* $ * $ * $ * 
$ * $ * $ * $
'''
#CODE:
n=7
for r in range(n):
    for c in range(n):
        if (r+c)%2!=0:
            print('*',end=' ')
        else:
            print('$',end=' ')
    print()
    
print('-'*70)
  
#11)
#O/P:
#CODE:





















