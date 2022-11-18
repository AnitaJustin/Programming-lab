def factors(k):
    a=[]
    for i in range(1,k+1):
        if k%i==0:
            a.append(i)
    return(a)
c=int(input("enter the number to find factors"))
print(f"the factos of the number {c} is {factors(c)}")
