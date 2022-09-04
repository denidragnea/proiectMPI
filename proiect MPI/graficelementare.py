from random import randint
from time import time
import matplotlib
from pylab import figure, show

def insertionSort(x):
    op=0
    for i in range(1,len(x)):
        aux=x[i]
        j=i-1
        while (aux<x[j]) and (j>=0):
            x[j+1]=x[j]
            j=j-1
            op=op+1
        x[j+1]=aux
    return x,op

def selectionSort(x):
    op=0 
    for i in range(0,len(x)-1):
        imin=i
        for j in range(i+1,len(x)):
            op=op+1
            if x[j]<x[imin]:
                imin=j
        if imin!=i:
            aux=x[i]
            x[i]=x[imin]
            x[imin]=aux
    return x,op        

def bubbleSort(x):
    op=0
    s=1
    while s==1:
        s=0
        for i in range(0,len(x)-1):
            op=op+1
            if x[i]>x[i+1]:
                aux=x[i]
                x[i]=x[i+1]
                x[i+1]=aux
                s=1
    return x,op


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