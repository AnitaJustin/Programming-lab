a=list(input("enter the integers").split(","))
for i in range(len(a)):
    if int(a[i])>100:
        a[i]="over"
        
print("the modified list :",a)
