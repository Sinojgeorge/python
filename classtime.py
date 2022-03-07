from tkinter.tix import InputOnly


class time:
    def __init__(self):
        self.hour=int(input("Enter the hopur:"))
        self.minute=int(input("enter the minute:"))
        self.second=int(input("entere the second:"))
    def _add_(self,value):
        return self.hour+value.hour,self.minute+value.minute,self.second+value.second
print("time1:")
t1=time()
print("time2:")
t2=time()
h=t1.hour + t2.hour
m=t1.minute+t2.minute
s=t1.second+t2.minute
print("sum of time t1&t2=",h,"hour",m,"minute",s,"second")

