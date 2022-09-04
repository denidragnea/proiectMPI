from random import randint
from time import time
import matplotlib
from pylab import figure, show

def quicksort0(x,s,d):
    if s<d:
        q,cp=pivot0(x,s,d)
        c1=quicksort0(x,s,q-1)
        c2=quicksort0(x,q+1,d)
        c=c1+c2+cp
    else:
        c=0
    return c

def pivot0(x,s,d):
    v=x[s]
    i=s
    c=0
    for j in range(s+1,d+1):
        if x[j]<=v:
            i+=1
            x[i],x[j]=x[j],x[i]
            c+=1
    x[i],x[s]=x[s],x[i]
    return i,c
    
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
    return i,c

def mergesort(x,s,d):
    c1=0
    c2=0
    c=0
    if s<d:
        m=(s+d)/2
        c1=mergesort(x,s,m)
        c2=mergesort(x,m+1,d)
        t,c=interclasare(x,s,m,d)
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
            if x[i]<=x[j]: 
                t[k]=x[i]
            i+=1
        else: 
            t[k]=x[j]
            j+=1
        k+=1
    #Se transfera eventualele elemente ramase in primul subtablou
    while i<=m:
        t[k]=x[i]
        i+=1
        k+=1
    #Se transfera eventualele elemente ramase in al 2lea subtablou
    while j<=d:
        t[k]=x[j]
        k+=1
        j+=1
    for i in range(s,d+1):
        x[i]=t[i-s]
    return t[0:k]


metode = {'bubbleSort':bubbleSort, 'selectionSort':selectionSort, 'insertionSort': insertionSort}
rezultate = {}
maxval = 2000
step = 100
marimi = range(2, maxval, step)
raport = 1
for marime in marimi:
    print ("Sortez o lista de dimensiunea", marime)
    lista = []
    maxrand = int(raport * marime)
    for i in range(0, marime):
        lista.append(randint(0, maxrand))
    for m in metode:
        if m not in rezultate:
            rezultate[m] = []
        #print ("Testez metoda",m,"cu",marime,"elemente")
        copie_lista = lista[:]
        t1 = time()
        metode[m](copie_lista)
        t2 = time()
        durata = t2 - t1
        rezultate[m].append(durata)


fig = figure()
ax = fig.add_subplot(111)
nume_metode = []
grafice_metode = []
for i in rezultate:
    r = ax.plot(marimi, rezultate[i], "-")
    grafice_metode.append(r)
    nume_metode.append(i)
ax.set_xlabel('Marime Lista')
ax.set_ylabel('Timp (secunde)')
ax.set_title('Timp de executie')
ax.legend(grafice_metode, nume_metode, loc=2)
fig.canvas.draw()
show()