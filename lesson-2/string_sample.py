
#name =input("What is your name?\n")
#age=int(input("How old are you?\n"))
#print("Hello " +name+ ". You are " + str(age) +" years old.")

# +  + is for string to join two strings. Note that it is only for strings
# to be able to join integers to sentences, we convert int to str first, then join them.

name1="Temur"
age1=17
#print(f"My name is {name1}, and I am {age1} years old.")

#f  ,  we can use f string and variables inside {}

#If we dont use f string , we need to format
#print("My name is {}, I am {} years old".format(name1, age1))
#or
#print("My name is {name}, and I am {Age} years old.".format(name=name1, Age=age1))


#To round up numbers in string
n=23.2342940
#print(f"{n:.2f}")


# so`zlarni bir qatorga keltirish uchun
name1="Temur"
name2="Xazratqulov"
#print(f"{name1:<11} - first name")
#print(f"{name2:<5} - last name")



mystr="Hello"
#print (len(mystr))
#len(variable) gives number of characters

#Sclising or Indexing
#Indexing is positioning of characters, and starts from 0



#print(mystr[4]) #shows 5th character
#print(mystr[1:4]) # Slicing #shows 2rd to 4th character
#index error
#sytax error
#type error
#value error
#print(mystr[:2] + mystr[4:]) #to cut some char
#[begin:end]     if empty, it starts from beginng or ends at the end
#[::n] show every nth char

#we can also use negative indexing, [-1:3], agar - indexdan foydanalansak, oxiridan boshlab o`rnini ko`rsatadi
#print(mystr[-6:-2])


#Mutable and Immutable


my_str="Apple"
#print(id(my_str))
my_str='a' + my_str[1:]
#print(my_str)
#print(id(my_str))



