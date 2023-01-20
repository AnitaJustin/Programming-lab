import csv
with open("salaries.csv",mode='r') as file:
    csvfile=csv.reader(file)
    l=[]
    for x in csvfile:
        l.append(x)
    print("columns")
    c=1
    for i in l[0]:
        print(c,":",i)
        c+=1
    lr=[int(x) for x in input("Enter column numbers:").split(" ")]
    print("lr=",lr)
    for i in lr:
        for x in l:
            print(x[i])
        print("\n")
        

