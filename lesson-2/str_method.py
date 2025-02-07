#methods

fruit="Apple and banana"
print(fruit.lower()) #to convert everychar to lowercase
#we can use Upper, Capitalize, Title and so on


print(fruit.startswith("A"))  #if it is true or false that it begins with A
print(fruit.title()) #to capitalize first letter of all words

#print('_'*50)
#word="              Hello WOrld              "
#print(word)
#print(word.strip())  #strip used to cut all spaces3
#fruits="apple banana cherry peach"
#print(fruits)
#print(fruits.split()) #to split the words


file_name='string_sample.py'
base_name=file_name.split('.')[0]
extension=file_name.split('.')[1]
print(file_name)
print(base_name)
print(extension)

#to take first letters of sentence
a=str(input("Write: "))
fl=[word[0] for word in a.split()]
re="".join(fl)
print(re)


