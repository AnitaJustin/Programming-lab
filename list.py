"""a=[]
n=int(input("enter the number of elements in the list:"))
for i in range(n):
    b=int(input("enter next element"))
    a.append(b)
p=[]
m=int(input("enter the number of elements in the list:"))
for i in range(m):
    c=int(input("enter next element"))
    p.append(c)
    """
a=input("enter the elements of list1:")
a=a.split(" ")
a=list(map(int,a))
p=input("enter the elements of list2:")
p=p.split(" ")
p=list(map(int,p))
n=len(a)
m=len(p)
if n==m:
    print("the lenght are same")
else:
    print("length are different")
sum1=0
for i in range(n):
    sum1+=int(a[i])

sum2=0
for i in range(m):
    sum2+=int(p[i])
if sum1==sum2:
    print("same sum")
else:
    print("the sum is different")
c=[]
for i in range(n):
    if a[i] in p:
        c.append(a[i])
   
print(f"the elements in both are",c)        
