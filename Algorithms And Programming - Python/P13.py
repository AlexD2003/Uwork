from logging.handlers import WatchedFileHandler
a=input()
a=int(a)
ca=a
cif=0
while(ca>0):
    ca//=10
    cif+=1
construction=0
while(cif>0):
    if(cif%2==1):
        construction=construction*10+a%10
    a//=10
    cif-=1
construction2=0
while(construction>0):
    construction2=construction2*10+construction%10
    construction//=10
print(construction2)