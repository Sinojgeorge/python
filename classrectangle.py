class rectangle():
    def __init__(self):
        self.length=int(input("enter the length:"))
        self.breadth=int(input("Enter the breadth:"))
    def area(self):
        return(self.length*self.breadth)
    def perimeter(self):
        return(2*(self.length+self.breadth))
r1=rectangle()
r2=rectangle()
print("area of rectangle=",r1.area())
print("perimeter of rectangle+",r1.perimeter())
print("area of rectangle=",r2.area())
print("perimeter of rectangle=",r2.perimeter())
if r1.area()==r2.area():
    print("areas are same")
else:
    print("areas are different")