st=input("enter a string: ")
feq={}
for i in st:
   if i in feq:
       feq[i]+=1
else:
    feq[i]=1
    print("count of characters in "+st+" is:\n"+str(feq))
