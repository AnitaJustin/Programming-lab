class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def perimeter(self):
        print("perimeter of rectangle =",(self.length*self.breadth))
    def area(self):
        print("area of rectangle =",2*(self.length+self.breadth))

rectangle_1=Rectangle(int(input("enter the length of first rectangle")),int(input("enter the breadth of first rectangle")))
rectangle_1.area()
rectangle_2=Rectangle(int(input("enter the length of second rectangle")),int(input("enter the breadth of second rectangle")))
rectangle_2.area()
