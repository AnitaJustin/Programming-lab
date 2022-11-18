def ingly(a):
    if a[-1]=="g" and a[-2]=="n" and a[-3]=="i":
        a.append("ly")
    else:
        a.append("ing")
    x=""
    for i in a:
        x+=i
    print(x)

j=list(input("enter the word"))
ingly(j)
