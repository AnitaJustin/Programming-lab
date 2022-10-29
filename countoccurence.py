a=list(input("enter the line of text:").split(" "))
c={}

for i in a:
    c[i]=0
    for j in a:
        if i==j:
            c[i]+=1
print(c)
