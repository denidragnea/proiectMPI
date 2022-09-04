from datetime import datetime
f1=open('fisier_100k_descrescator.txt','r')
f2=open('fisier_100k_crescator_an.txt','w')

x=[]
start=datetime.now()

def BubbleSort(x):
    for j in range(len(x)-1,0,-1):
        for i in range(j):
            if x[i]>x[i+1]:
                aux=x[i]
                x[i]=x[i+1]
                x[i+1]=aux
    return x
	
with open('fisier_100k_descrescator.txt','r') as f1:
    for line in f1:
        x.extend(map(int,line.split(',')))

y=len(x)
x=BubbleSort(x)

print("Acesta este timpul necesar sortarii: ",datetime.now()-start)

for i in range(0,len(x )):
    f2.write(str(x[i]))
    if i!=y-1:
        f2.write(', ')
f2.close()