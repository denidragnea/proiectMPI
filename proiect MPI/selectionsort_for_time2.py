from datetime import datetime
#f1=open('fisier_100k_crescator.txt','r')
#f2=open('fisier_1k_crescator_an.txt','w')

x=[]
start=datetime.now()

def selection(x):
    for i in range(0,len(x)-1):
        k=i
        for j in range(i+1,len(x)):
            if x[k]>x[j]:
                k=j
        if k!=i:
            aux=x[i]
            x[i]=x[k]
            x[k]=aux
    return x

with open('fisier_100k_crescator.txt','r') as f1:
    for line in f1:
        x.extend(map(int,line.split(',')))

y=len(x)
x=selection(x)

print("Acesta este timpul necesar sortarii: ",datetime.now()-start)
"""
for i in range(0,len(x )):
    f2.write(str(x[i]))
    if i!=y-1:
        f2.write(', ')
f2.close()

"""
