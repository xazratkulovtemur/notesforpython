#class Length:
 #   def __init__ (self):
  #      pass
   # 
    #def all(self):
     #   leng=int(input("Enter the length: "))
      #  n=int(input("How many times you come and go: "))
       # return leng*n
        

#length1=Length()
#print(length1.all())

class Vector:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
v1=Vector(1,2)
v2=Vector(2,3)
class Number:
    def __init__(self, value):
        self.value=value
    def __add__(self, other):
        return self.value + other.value
n1=Number(15)
n2=Number(15)
print(n1+n2)
class Floor:
    def __init__(self, value):
        self.value=value
    def __truediv__(self, other):
        return self.value/other.value
    
p1=Floor(10)
p2=Floor(3)
result=p1/p2
print(result)

class Collection:
    def __init__(self, items):
        self.items=items
    def __getitem__(self, index):
        return self.items[index]
    
    
    def __len__(self):
        return len(n)


n=Collection([1,2,3,4,5])
length=len(n)
index=int(input("Enter index: "))
if index<length:
    print(n[index])
else:
    print("Index is out of range!")
