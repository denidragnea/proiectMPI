#pentru sortarea unei liste crescatoare trebuie interschimbate capetele intervalului



from datetime import datetime
f2=open('scrie.txt','w')

x=[]
start=datetime.now()

def quicksort0(x,s,d):
        if s<d:
             q=pivot0(x,s,d)
             quicksort0(x,s,q)
             quicksort0(x,q+1,d)
        return x[s:d+1]

def pivot0(x,s,d):
    v=x[s]
    i=s
    for j in range(s+1,d+1):
        if x[j]<=v:
             i+=1
             x[i],x[j]=x[j],x[i]
    x[i],x[s]=x[s],x[i]
    return i

with open('fisier_10k_descrescator.txt','r') as f1:
    for line in f1:
        x.extend(map(int,line.split(',')))

y=len(x)
x=quicksort0(x,0,len(x)-1)


print("Acesta este timpul necesar sortarii: ",datetime.now()-start)


for i in range(0,len(x)):
    f2.write(str(x[i]))
    if i!=y-1:
        f2.write(', ')
f2.close()

