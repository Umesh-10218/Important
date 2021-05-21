data ='my love name is jhanu but she hates me a lot'

AJ=open('AmulJhan.txt','w')

AJ.write(data)

AJ.close()

print('-'*60)

AMUL=open('AmulJhan.txt','r')

res=AMUL.read()

print(res)

AMUL.close()




print('-'*60)



