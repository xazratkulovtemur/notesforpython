import json


input=r"D:\MAAB academy new\python\notesforpython\lesson-9\student.json"

data = {
    "students": [
        {"name": "Alice", "math": 85, "science": 78, "english": 92},
        {"name": "Bob", "math": 76, "science": 88, "english": 70},
        {"name": "Charlie", "math": 90, "science": 95, "english": 85}
    ]
}
with open (input, 'wt') as file:
    content=json.dump(data,file, indent=4)
print("Datat stored in json file")

with open(input, 'r') as file:
    content=json.load(file)
    print(content)
    

new_student = {"name": "David", "math": 50, "science": 60, "english": 55}
content["students"].append(new_student)    #adding new student
for student in content["students"]:
    if student["name"]=="Bob":
        student["math"]=90 #updating data

with open(input, 'wt') as file:
    writer=json.dump(content, file, indent=4)


sorted_by_math=sorted(content["students"], key=lambda x: x["math"], reverse=True)
print(sorted_by_math)
