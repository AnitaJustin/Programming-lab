class Publisher:
    def __init__(self,name):
        self.name=name
class Book(Publisher):
   def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
   def display(self):
        print(self.name)
        print(self.title)
        print(self.author)
class Python(Book):
    def __init__(self,name,title,author,price,no_of_pages):
        super().__init__(name,title,author)
        self.price=price
        self.no_of_pages=no_of_pages
    def display(self):
        print("Publisher:",self.name)
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price",self.price,"\n","No.of pages",self.no_of_pages)
p=input("Enter publisher name:")
t=input("Enter book title:")
a=input("Enter author:")
pr=input("Enter price:")
pages=input("Enter no of pages:")
b1=Python(p,t,a,pr,pages)
b1.display()

