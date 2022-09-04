def BubbleSort(x):
    for j in range(len(x)-1,0,-1):
        for i in range(j):
            if x[i]>x[i+1]:
                aux=x[i]
                x[i]=x[i+1]
                x[i+1]=aux
    return x
x=[2,1,4,5,3,0]
print (BubbleSort(x))