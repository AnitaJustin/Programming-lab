def factorial(x):
    product=1
    for i in range(1,x+1):
        product=product*i
    return(product)
n=int(input("enter the number to find the factorial"))
print(f"the factorial of {n} is {factorial(n)}")

        
