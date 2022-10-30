# find GCD of a list of numbers
a=list(map(int,input("enter the two numbers").split(" ")))
c=[]
for i in range(1,a[0]+1):
    count=0
    for j in a:
        if j%i==0:
            count+=1
    if count==len(a):
        c.append(i)
b=0
for i in c:
    if i>b:
        b=i
print(f"the gcd of the given list of numbers is :{b}")
