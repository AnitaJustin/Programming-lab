#accept a file name from user and print extension of that
a=list(input("enter the file name"))
for i in range(len(a)):
    if a[i]==".":
        break
x=""
for j in range(i+1,len(a)):
    x+=a[j]
print(x,"is the extension of the file")
