string=input("Enter a string:")
word=string.split()
d={}
for w in word:
    if w in d:
        d[w]+=1
    else:
        d[w]=1
        for x in d.keys():
            print("%s occurance %s times"%(x,d[x]))
