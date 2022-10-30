#take a number as an input and find the sequence N+NN+NNN+NNNN+.....
N=int(input("enter the number"))
n=int(input("enter the number of terms"))
res=0
for i in range(1,n+1):
    p=1 
    for j in range(1,i+1):
        p=p*N
    res+=p
print(res)    
