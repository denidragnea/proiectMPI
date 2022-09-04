from datetime import datetime
c=0
x=[]

def quicksort1(x,s,d):
    if s<d:
        q,cp=pivot1(x,s,d)
        c1=quicksort1(x,s,q-1)
        c2=quicksort1(x,q+1,d)
        c=c1+c2+cp
    else:
        c=0
    return c

def pivot1(x,s,d):
    v=x[d]
    i=s-1
    j=d
    c=0
    while i<j:
        c+=1
        while True:
            i+=1
            c+=1
            if x[i]>=v:
                break
        while True:
            j-=1
            c+=1
            if x[j]<=v:
                break
        if i<j:
            c+=1
            x[i],x[j]=x[j],x[i]
    x[i],x[d]=x[d],x[i]
    c+=1
    return i,c

with open('fisier_10k_crescator.txt','r') as f1:
    for line in f1:
        x.extend(map(int,line.split(',')))

c=quicksort1(x,0,len(x)-1)

print("Numarul de operatii necesar sortarii: ",c)
