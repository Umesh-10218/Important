n=int(input('Enter the number of units'))
def electricitybill(n):
    
    while n!=0:
        if dom_u:
            fxdp=60
            
            if n<=30:
                amt=(n*3.75)
            elif n<=100:
                amt=(30*3.75)+((n-30)*5.2)
            elif n<=200:
                amt=(30*3.75)+((n-30)*5.2)+((n-130)*6.75)
            elif n>200:
                amt=(30*3.75)+((n-30)*5.2)+((n-130)*6.75+((n-200)*7.8)
                                            totalamt=amt+fxdp
                                            tax=0.05*totalamt
                                            res=totalamt+tax
                                            print ('Total =',res)
        else:
            if dom_r:
                fxdp=45
            
            if n<=30:
                amt=(n*3.65)
            elif n<=100:
                amt=(30*3.65)+((n-30)*4.9)
            elif n<=200:
                amt=(30*3.65)+((n-30)*4.9)+((n-130)*6.45)
            elif n>200:
                amt=(30*3.65)+((n-30)*4.9)+((n-130)*6.45)+((n-200)*7.3)
             totalamt=amt+fxdp
             tax=0.05*totalamt
             res=totalamt+tax
            print('Total =',res)
