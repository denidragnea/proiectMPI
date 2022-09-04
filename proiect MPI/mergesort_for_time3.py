from datetime import datetime
x=[]
start=datetime.now()

def interclasare(x,s,m,d):
    i=s
    j=m+1
    k=0
    t=[0]*(d-s+1)
    #Se parcurg subtablourile in paralel si la fiecare pas se transfera cel mai mic element
    while i<=m and j<=d:
        if x[i]<=x[j]: #Transfer din subtabloul x[s..m]
            t[k]=x[i]
            i+=1
        else: #Transfer din subtabloul x[m+1..d]
            t[k]=x[j]
            j+=1
        k+=1
    #Se transfera eventualele elemente ramase in primul subtablou
    while i<=m:
        t[k]=x[i]
        i+=1
        k+=1
    #Se transfera eventualele elemente ramase in al 2lea subtablou
    while j<=d:
        t[k]=x[j]
        k+=1
        j+=1
    for i in range(s,d+1):
        x[i]=t[i-s]
    return t[0:k]

def sortare(x,s,d):
    if s<d:
        m=(s+d)/2
        x[s:m+1]=sortare(x,s,m)
        x[m+1:d+1]=sortare(x,m+1,d)
        x[s:d+1]=interclasare(x,s,m,d)
    return x[s:d+1]


with open('fisier_10kk_descrescator.txt','r') as f1:
    for line in f1:
        x.extend(map(int,line.split(',')))

y=len(x)
x=sortare(x,0,len(x)-1)

print("Acesta este timpul necesar sortarii: ",datetime.now()-start)
