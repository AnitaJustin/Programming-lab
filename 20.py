#from a list of integers,create a list removing even numbers
a=list(map(int,input("enter the numbers of list separated by space:").split(" ")))
c=[x for x in a if x%2!=0]
print(c)
