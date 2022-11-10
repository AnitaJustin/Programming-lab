a={}
b={}
c={}
n=int(input("enter the number of keys"))
for i in range(0,n):
    key=input("emter the key value")
    a[key]=input("enter the value")
m=int(input("enter the number of keys in dict2"))
for i in range(0,m):
    key=input("enter the key value")
    b[key]=input("enter the value")
print(a)
print(b)
c={**a,**b}
for j,l in c.items():
    if j in a.keys() and j in b.keys():
        c[j]=[l,a[j]]

print(c)
