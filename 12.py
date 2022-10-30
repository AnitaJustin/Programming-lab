#get an input string where all occurance of first character replaced with $ except first character
a=list(input("enter the string"))
for i in range(1,len(a)):
    if a[i]==a[0]:
        a[i]="$"
x=""
for i in a:
    x+=i
print(x)
        
        

