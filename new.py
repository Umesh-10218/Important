'''def strng(self,name,flag):
    self.name=name
    self.flag=flag
    for i in name :
        res=' '
        if flag==0:
            res+=name[1::2]
            print(res)
        else:
            res+=name[::2]
            print(res)

fun=strng(self,"Tracxn",0)
fu=strng(self,"Traxcn",1)
'''


def strng(name,flag):
    res=' '
    if flag==0:
        res+=name[1::2]
        print(res)
    else:
        res+=name[::2]
        print(res)
strng("TRACXN",0)
strng("TRACXN",1)
