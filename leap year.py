a=int(input("enter the present year"))
b=int(input("enter the final year"))
c=[]
for i in range(a,b+1):
    if i%4==0:
        if i%100==0:
            if i %400==0:
                c.append(i)
        else:
            c.append(i)
print(c)
