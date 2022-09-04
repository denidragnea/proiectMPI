import random

f=open('fisier_1k_nouXX.txt','w')
n=1000
for i in range(0,n):
    x=random.randint(-9999,9999)
    f.write(str(x))
    if i!=n-1:
        f.write(',')
f.close()
