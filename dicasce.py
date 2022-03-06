from pickle import TRUE
y={'carl':40,'alan':2,'bob':1,'dany':3}
l=list(y.items())
dict=dict(l)
print("dictinory:",dict)
l.sort()
print("ascending order is:",l)
l=list(y.items())
l.sort(reverse=True)
print("decending order is",l)
