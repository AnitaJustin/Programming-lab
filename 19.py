#create a single string separated with space from 2 strings by swapping the character at position 1
a=list(input("enter first string"))
b=list(input("enter second string"))
a[0],b[0]=b[0],a[0]
x=""
for i in a:
    x+=i
x=x+" "
for i in b:
    x+=i
print(x)    
