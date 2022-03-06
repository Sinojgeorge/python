listl=[11,12,13,17,22,6,323]
print("the original list is:",listl)
for i in listl:
    if(0==i%2):
        listl.remove(i)
        print("List after removing even numbers is:",listl)
