startyear=int(input("enter start year:"))
endyear=int(input("enter end year:"))
print("list of leap years:\n")
for year in range(startyear,endyear):
    if(0==year%4):
     print(year)