import os
if os.path.exists('merged.txt'):
    print("File exists")
else:
    print("Not exist")
with open("text1.txt", 'r') as file:
    first=file.readlines()

with open("text2.txt", 'r') as file:
    second=file.readlines()

with open('merged.txt', 'w') as file:
    file.writelines(first + second)