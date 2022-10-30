#print out all colors from color list1 not contained in color list2
colorlist1=list(input("enter the colors").split(" "))
colorlist2=list(input("enter the color of list2").split(" "))
for i in colorlist1:
    if i not in colorlist2:
        print(i)
