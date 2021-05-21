#OBJECT METHOD:
#1)
#O/P:
'''
raju 25 8265314789
ramu 26 8679456123
raju 25 8265314789
ramu 26 8679456123
'''
#CODE:
class school:
    sn='chaitanya'
    cm='ramappa'
    loc='vjd'
    nos=0
    def __init__(self,sname,age,phno):
        school.nos+=1
        self.sid=school.nos
        self.sname=sname
        self.age=age
        self.phno=phno
    def disp_stu(self):
        print(self.sid,self.sname,self.age,self.phno)
raju=school('raju',25,8265314789)
ramu=school('ramu',26,8679456123)

#Calling W.R.T Object:

raju.disp_stu()
ramu.disp_stu()

#Calling W.R.T Classname:

school.disp_stu(raju)
school.disp_stu(ramu)

print('-'*70)

#2)
#O/P:

#CODE:
class RBI:
    nb='SBI'
    roi= 14.6
    mbl='Delhi'
    b=0
    def __init__(self,bname,loc,mgr,ifsc):
        RBI.b+=1
        self.bid=RBI.b
        self.bname=bname
        self.loc=loc
        self.mgr=mgr
        self.ifsc=ifsc

    def disp_bank(self):
        print(self.bid,self.bname,self.loc,self.mgr,self.ifsc)

MUM=RBI('SBI OF MUM','MUMBAI','RAMAPPA','SBIN0040672')
BANG=RBI('SBI OF BANG','BANGALORE','THIMAPPA','SBIN0040618')
HYD=RBI('SBI OF HYD','HYDERABAD','RAJAPPA','SBIN0048965')

#Calling W.R.T Object:
MUM.disp_bank()
BANG.disp_bank()
HYD.disp_bank()

#Calling W.R.T Classname:

RBI.disp_bank(MUM)
RBI.disp_bank(BANG)
RBI.disp_bank(HYD)

print('-'*70)


#1)
#O/P:
#CODE:
print('-'*70)



#1)
#O/P:
#CODE:
print('-'*70)





#1)
#O/P:
#CODE:
print('-'*70)





