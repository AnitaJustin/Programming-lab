#create a list of comma separated color names from user and display first and last color
a=list(input("enter a list of color names").split(","))
print(f"the first color is {a[0]} and the last color is {a[len(a)-1]}")
