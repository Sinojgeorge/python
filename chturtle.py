
def circlearea(r):
    return 3.14*(r*r)
def circleperi(r):
    return 2*3.14*r
def rectarea(l,b):
    return l*b
def rectperi(l,b):
    return 2*(l+b)
def spherearea(sr):
    return (4*3.14*sr*sr)
def sphereperi(sr):
    return (1.33*3.14*sr*sr*sr)
def cuboidarea(cl,w,h):
    return (4*(cl+w+h))
def cuboidperi(cl,w,h):
    return((2*cl*w)+(2*cl*h)+(2*w*h))
print("select operration")
print("1.rectangle")
print("2.circle")
print("3.sphere")
print("4.cuboid")
while True:
    choice=input("enter (1/2/3/4):")
    if choice in('1','2','3','4'):
        if choice=='1':
            l=int(input("Enter the length of rectangle:"))
            b=int(input("enter the breadth of rectangle:"))
            print("area of rectangle=",rectarea(l,b))
            print("perimeter of rectangle=",rectperi(l,b))
        if choice=='2':
            r=int(input("enter the radius of circle"))
            print("area of circle=",circlearea(r))
            print("the perimeter of circle is=",circleperi(r))
        if choice=='3':
            sr=int(input("enter radius of sphere:"))
            print("area of sphere is=",spherearea(sr))
            print("perimeter of spher =",sphereperi(sr))
        if choice=='4':
            cl=int(input("enter the length of cuboid"))
            w=int(input("enter the width of cuboid:"))
            h=int(input("enter the height of cuboid"))
            print("area of cuboid=",cuboidarea(cl,w,h))
            print("perimeter of cuboid is=",cuboidperi(cl,w,h))
        if choice=='5':
            exit(0)
        else:
            print("invalid input")



