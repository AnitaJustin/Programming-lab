a={}
b={}
c={}
n=int(input("enter the number of keys"))
for i in range(0,n):
    key=input("emter the key value")
    a[key]=input("enter the value")
b=sorted(a.items())
print(b)
c=sorted(a.items(),reverse=True)
print(c)
