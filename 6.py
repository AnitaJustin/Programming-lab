def frequency():
    d={}
    a=list(input("enter the string:"))
    for i in a:
        count=0
        for j in a:
            if i==j:
                count+=1
        d[i]=count
    print(d)
                
frequency()
