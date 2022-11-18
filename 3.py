def add(a):
    res=0
    for i in range(len(a)):
        res=res+a[i]
    return(res)
a=list(map(int,input("enter the numbers of the list").split(" ")))
print("the sum of the elements of the list is:",add(a))
