class rectangle():
    __length=None
    __width=None
    def __init__(self):
        self.length=int(input("Enter the length"))
        self.width=int(input("Enter the width"))
    def area(self):
        return(self.length*self.width)
r1=rectangle()
r2=rectangle()
print("The area of rectangle",r1.area())
print("the area of rectangle 2",r2.area())
if r1.area()<r2.area():
    print("area of r2 is greater")
else:
    print("area of r1 is greater")