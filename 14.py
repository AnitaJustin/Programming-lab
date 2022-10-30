#find the biggest number of 3
a=list(map(int,input("enter 3 numbers with space").split(" ")))
b=0
for i in a:
   if i>b:
       b=i
print(b,"is the greatest number")

