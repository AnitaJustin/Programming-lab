class Rectangle:
    def __init__(self,length,width):
        self._length=length
        self._width=width
    def area(self):
        return self._length*self._width
    def __lt__(self,other):
        if(self.area()<other.area()):
            print("1st recatngle is smaller")
        else:
            print("2nd rectangle is smaller")
l1=int(input("enter length 1:"))
l2=int(input("enter length 2:"))
w1=int(input("enter width 1:"))
w2=int(input("enter width 2:"))
r1=Rectangle(l1,w1)
r2=Rectangle(l2,w2)
r1<r2 
