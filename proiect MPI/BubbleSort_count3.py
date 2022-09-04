from datetime import datetime
c=0
x=[]

def BubbleSort(x):
	c=0
    for j in range(len(x)-1,0,-1):
        for i in range(j):
            if x[i]>x[i+1]:
				c+=1
                aux=x[i]
                x[i]=x[i+1]
                x[i+1]=aux
    return c
	
with open('fisier_100k_descrescator.txt','r') as f1:
    for line in f1:
        x.extend(map(int,line.split(',')))

c=BubbleSort(x)

print ("Numarul de operatii necesar sortarii: ",c)