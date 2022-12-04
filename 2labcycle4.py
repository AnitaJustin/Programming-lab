#generate a list of 4 digit numbers in a given range with all their digits even and the number is a perfect square
from math import *
p,q=input("enter the range separated by space").split(" ")
b=[]
for i in range(int(p),int(q)+1):
    j=i
    s=0
    while(j>0):
        rem=j%10
        if rem%2==0:
            j=j//10
            s+=1
        else:
            break
    if(s==4):
        k=int(sqrt(i))
        if (k*k==i):
            b.append(i)
print(b)
        
