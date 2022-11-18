def fibonacci(n):
    c=[1,1]
    for i in range(2,n):
        c.append(c[i-1]+c[i-2])
    print(c)
k=int(input("enter the number of terms:"))
fibonacci(k)
