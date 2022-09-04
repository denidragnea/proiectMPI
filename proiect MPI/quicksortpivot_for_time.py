from datetime import datetime
#f2=open('scrie.txt','w')

x=[]
start=datetime.now()

def quicksort(x,s,d):
    if s<d:
        q=pivot(x,s,d)
        x[s:q]=quicksort(x,s,q-1)
        x[q+1:d+1]=quicksort(x,q+1,d)
    return x[s:d+1]

def pivot(x,s,d):
    v=x[d]
    i=s-1
    j=d
    c=0
    while i<j:
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
            x[i],x[j]=x[j],x[i]
    x[i],x[d]=x[d],x[i]
    return i


with open('fisier_10kk_aleator.txt','r') as f1:
    for line in f1:
        x.extend(map(int,line.split(',')))

y=len(x)
x=quicksort(x,0,len(x)-1)

print("Acesta este timpul necesar sortarii: ",datetime.now()-start)
"""
for i in range(0,len(x )):
    f2.write(str(x[i]))
    if i!=y-1:
        f2.write(', ')
f2.close()
"""
