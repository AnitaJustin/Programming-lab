#create a string from a given string where the first and last letters are interchanged
a=list(input("enter the string"))
a[0],a[len(a)-1]=a[len(a)-1],a[0]
x=""
for i in a:
    x+=i
print(x)
