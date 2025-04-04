month=["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
keys=[1,2,3,4,5,6,7,8,9,10,11,12]


dict1={k:v for (k,v) in zip(keys, month)} 
month=int(input("Enter month: "))
day=int(input("Enter date: "))

year=int(input("Enter year: "))

print(month,"/",day,"/",year)
print("-"*50)

print(dict1[month], day, ",", year)
print("-"*50)

print(day, dict1[month], year)