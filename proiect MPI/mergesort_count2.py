from datetime import datetime
c=0
x=[]

def mergesort(x,s,d):
    c1=0
    c2=0
    c=0
    if s<d:
        m=(s+d)/2
        c1=mergesort(x,s,m)
        c2=mergesort(x,m+1,d)
        t,c=interclasare(x,s,m,d)
    else:
        c=0
    return c1+c2+c

def interclasare(x,s,m,d):
    t=[0]*(d-s+1)
    i=s
    j=m+1
    k=0
    c=0
    while i<=m and j<=d:
        c+=1
        while i<=m and j<=d:
            if x[i]<=x[j]: #Transfer din subtabloul x[s..m]
                t[k]=x[i]
                i+=1
                c+=1
            else: #Transfer din subtabloul x[m+1..d]
                t[k]=x[j]
                j+=1
                c+=1
            k+=1
    #Se transfera eventualele elemente ramase in primul subtablou
    while i<=m:
        t[k]=x[i]
        i+=1
        k+=1
        c+=1
    #Se transfera eventualele elemente ramase in al 2lea subtablou
    while j<=d:
        t[k]=x[j]
        k+=1
        j+=1
        c+=1
    for i in range(s,d+1):
        x[i]=t[i-s]
        c+=1
    return t[0:k],c

with open('fisier_100k_crescator.txt','r') as f1:
    for line in f1:
        x.extend(map(int,line.split(',')))

c=mergesort(x,0,len(x)-1)

print("Numarul de operatii necesar sortarii: ",c)

