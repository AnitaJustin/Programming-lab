a=list(input("enter the first names").split(","))
count=0
for i in a:
    for j in i:
        if j=="a":
            count+=1
print("number of a's in first names:",count)

