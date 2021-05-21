#CLASS AND OBJECTS
#1)Creation of Class and Object:
#O/P:
'''
<__main__.school object at 0x000000F3E7573F88>
<__main__.school object at 0x000000F3E7573F48>
<__main__.school object at 0x000000F3E77FF608>
<__main__.school object at 0x000000F3E77FF808>
'''
#CODE:
class school:    
    sname='shs'
    chairman='abc'
    mbl='vjw'
gn=school()
sc=school()
hb=school()
vc=school()

print(gn)
print(sc)
print(hb)
print(vc)

print('*'*80)

#2)Class n Object values display:
#O/P:
'''
<__main__.school object at 0x000000D7F74EC608>
shs abc vjw
<__main__.school object at 0x000000D7F72B3FC8>
shs abc vjw
<__main__.school object at 0x000000D7F753F4C8>
shs abc vjw
<__main__.school object at 0x000000D7F753F708>
shs abc vjw
'''
#CODE:
class school:
    sname='shs'
    chairman='abc'
    mbl='vjw'
gn=school()
sc=school()
hb=school()
vc=school()

print(gn)
print(gn.sname,gn.chairman,gn.mbl)
print(sc)
print(sc.sname,sc.chairman,sc.mbl)
print(hb)
print(hb.sname,hb.chairman,hb.mbl)
print(vc)
print(vc.sname,vc.chairman,vc.mbl)

print('*'*80)


#3)Modification w.r.t class: 
#O/P:
'''
<__main__.school object at 0x0000003FA789FCC8>
shs abc vjw
<__main__.school object at 0x0000003FA789F588>
shs abc vjw
<__main__.school object at 0x0000003FA784C708>
shs abc vjw
<__main__.school object at 0x0000003FA789F3C8>
shs abc vjw
********************************************************************************
<__main__.school object at 0x0000003FA789FCC8>
shs abc hyd
<__main__.school object at 0x0000003FA789F588>
shs abc hyd
<__main__.school object at 0x0000003FA784C708>
shs abc hyd
<__main__.school object at 0x0000003FA789F3C8>
shs abc hyd
'''
#CODE:
class school:
    sname='shs'
    chairman='abc'
    mbl='vjw'
gn=school()
sc=school()
hb=school()
vc=school()

print(gn)
print(gn.sname,gn.chairman,gn.mbl)
print(sc)
print(sc.sname,sc.chairman,sc.mbl)
print(hb)
print(hb.sname,hb.chairman,hb.mbl)
print(vc)
print(vc.sname,vc.chairman,vc.mbl)

print('*'*80)

school.mbl='hyd'

print(gn)
print(gn.sname,gn.chairman,gn.mbl)
print(sc)
print(sc.sname,sc.chairman,sc.mbl)
print(hb)
print(hb.sname,hb.chairman,hb.mbl)
print(vc)
print(vc.sname,vc.chairman,vc.mbl)

print('*'*80)

#4)Modification w.r.t Object:
#O/P:
'''
shs abc vjw
shs abc vjw
shs abc vjw
shs abc vjw
********************************************************************************
shs pqr vjw
shs stu vjw
shs mno vjw
shs uvw vjw
'''
#CODE:
class school:
    sname='shs'
    chairman='abc'
    mbl='vjw'
gn=school()
sc=school()
hb=school()
vc=school()

print(gn.sname,gn.chairman,gn.mbl)
print(sc.sname,sc.chairman,sc.mbl)
print(hb.sname,hb.chairman,hb.mbl)
print(vc.sname,vc.chairman,vc.mbl)

print('*'*80)

gn.chairman='pqr'
sc.chairman='stu'
hb.chairman='mno'
vc.chairman='uvw'

print(gn.sname,gn.chairman,gn.mbl)
print(sc.sname,sc.chairman,sc.mbl)
print(hb.sname,hb.chairman,hb.mbl)
print(vc.sname,vc.chairman,vc.mbl)

print('*'*80)

#5)Using of CONSTRUCTOR(--INIT--):
#O/P:
'''
shs abc vjw GANDHINAGAR SHIVANAND BALLARI
shs abc vjw SUDHACROSS RAMMURTHY SUDHACIRCLE
shs abc vjw HAVAMBAVI MADHUSUDHAN HAVAMBAVI
shs abc vjw VASAVI CAMPUS SRIRAMULU INFANTRY ROAD
********************************************************************************
shs abc vjw GANDHINAGAR SHIVANAND BALLARI
shs abc vjw SUDHACROSS RAMMURTHY SUDHACIRCLE
shs abc vjw HAVAMBAVI MADHUSUDHAN HAVAMBAVI
shs abc vjw VASAVI CAMPUS SRIRAMULU INFANTRY ROAD
'''
#CODE:
class school:
    sname='shs'
    chairman='abc'
    mbl='vjw'
    def __init__(self,bchn,prin,loc):
        self.bchn=bchn
        self.prin=prin
        self.loc=loc
    def res(self):
        print(self.sname,self.chairman,self.mbl,self.bchn,self.prin,self.loc)
gn=school('GANDHINAGAR','SHIVANAND','BALLARI')
sc=school('SUDHACROSS','RAMMURTHY','SUDHACIRCLE')
hb=school('HAVAMBAVI','MADHUSUDHAN','HAVAMBAVI')
vc=school('VASAVI CAMPUS','SRIRAMULU','INFANTRY ROAD')
#calling w.r.t objname:
gn.res()
sc.res()
hb.res()
vc.res()
print('*'*80)

#calling w.r.t classname:
school.res(gn)
school.res(sc)
school.res(hb)
school.res(vc)

print('*'*80)



#6)
#O/P:
'''
shs pqr VIZAG GANDHINAGAR SHIVANAND BALLARI
shs stu VIZAG SUDHACROSS RAMMURTHY SUDHACIRCLE
shs mno VIZAG HAVAMBAVI MADHUSUDHAN HAVAMBAVI
shs uvw VIZAG VASAVI CAMPUS SRIRAMULU INFANTRY ROAD
********************************************************************************
shs pqr hyd GANDHINAGAR SHIVANAND BALLARI
shs stu hyd SUDHACROSS RAMMURTHY SUDHACIRCLE
shs mno hyd HAVAMBAVI MADHUSUDHAN HAVAMBAVI
shs uvw hyd VASAVI CAMPUS SRIRAMULU INFANTRY ROAD
'''
#CODE:
class school:
    sname='shs'
    chairman='abc'
    mbl='vjw'
    def __init__(self,bchn,prin,loc):
        self.bchn=bchn
        self.prin=prin
        self.loc=loc
    def res(self):
        print(self.sname,self.chairman,self.mbl,self.bchn,self.prin,self.loc)
gn=school('GANDHINAGAR','SHIVANAND','BALLARI')
sc=school('SUDHACROSS','RAMMURTHY','SUDHACIRCLE')
hb=school('HAVAMBAVI','MADHUSUDHAN','HAVAMBAVI')
vc=school('VASAVI CAMPUS','SRIRAMULU','INFANTRY ROAD')


gn.chairman='pqr'
sc.chairman='stu'
hb.chairman='mno'
vc.chairman='uvw'

school.mbl='VIZAG'

#calling w.r.t objname:
gn.res()
sc.res()
hb.res()
vc.res()
print('*'*80)

school.mbl='hyd'


#calling w.r.t classname:
school.res(gn)
school.res(sc)
school.res(hb)
school.res(vc)

print('*'*80)
