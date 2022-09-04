import random

f=open('fisier_10k_nouXX.txt','w')
n=10000
for i in range(0,n):
    x=random.randint(-99999,99999)
    f.write(str(x))
    if i!=n-1:
        f.write(',')
f.close()
