num=int(input("Enter a number:"))
for row in range(1,num+1):
    print("\t")
    for col in range(1,row+1):
        print(row*col,end="\t")