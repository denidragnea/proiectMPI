import random

f=open('fisier_100k_nouXX.txt','w')
n=100000
for i in range(0,n):
    x=random.randint(-999999,999999)
    f.write(str(x))
    if i!=n-1:
        f.write(',')
f.close()
