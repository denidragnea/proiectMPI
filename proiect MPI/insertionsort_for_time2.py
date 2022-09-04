from datetime import datetime
f1=open('fisier_100k_crescator.txt','r')
f2=open('fisier_100k_crescator_an.txt','w')

x=[]
start=datetime.now()

def insertion(x):
    for i in range(1,len(x)):
        aux=x[i]
        j=i-1
        while j>=0 and aux<x[j]:
            x[j+1]=x[j]
            j=j-1
        x[j+1]=aux
    return x

with open('fisier_10k_crescator.txt','r') as f1:
    for line in f1:
        x.extend(map(int,line.split(',')))

y=len(x)
x=insertion(x)

print("Acesta este timpul necesar sortarii: ",datetime.now()-start)

for i in range(0,len(x )):
    f2.write(str(x[i]))
    if i!=y-1:
        f2.write(', ')
f2.close()



