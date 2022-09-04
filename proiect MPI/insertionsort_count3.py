from datetime import datetime
c=0
x=[]

def insertion(x):
    c=0
    for i in range(1,len(x)):
        c+=1
        aux=x[i]
        j=i-1
        while j>=0 and aux<x[j]:
            c+=1
            x[j+1]=x[j]
            j=j-1
        x[j+1]=aux
    return c

with open('fisier_100k_descrescator.txt','r') as f1:
    for line in f1:
        x.extend(map(int,line.split(',')))

c=insertion(x)

print ("Numarul de operatii necesar sortarii: ",c)
