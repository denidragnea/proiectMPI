from datetime import datetime
c=0
x=[]

def selection(x):
    c=0
    for i in range(0,len(x)-1):
        c+=1
        k=i
        for j in range(i+1,len(x)):
            c+=1
            if x[k]>x[j]:
                c+=1
                k=j
        if k!=i:
            c+=1
            aux=x[i]
            x[i]=x[k]
            x[k]=aux
    return c

with open('fisier_100k_crescator.txt','r') as f1:
    for line in f1:
        x.extend(map(int,line.split(',')))

c=selection(x)

print ("Numarul de operatii necesar sortarii: ",c)
