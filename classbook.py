class publisher():
    def __init__(self):
        self.name="prentice Hall"
    def display(self):
        print("publisher is",self.name)
class book(publisher):
    def __init__(self):
        self.title="Core Python Application Programming"
        self.author="Wesley j Chun"
    def display(self):
        super().__init__()
        super().display()
        print("title",self.title)
        print("author",self.author)
class python(book):
    def __init__(self):
        self.price="1176"
        self.pages="2352"
    def display(self):
        super().__init__()
        super().display()
        print("price",self.price)
        print("no of pages",self.pages)
obj2=python()
print("book details are:\n")
obj2.display()