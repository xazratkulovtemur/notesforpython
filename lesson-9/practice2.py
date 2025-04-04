import csv
input=r"D:\MAAB academy new\python\notesforpython\lesson-9\students_score.csv"
output=r"D:\MAAB academy new\python\notesforpython\lesson-9\students_report.csv"
filtered_data=[]

with open(input, 'rt') as file:
    reader=csv.reader(file)
    header=next(reader)
    data=list(reader)

header.append("Average score")
header.append("Status")

for row in data:
    name=row[0]
    math=row[1]
    science=row[2]
    english=row[3]
    average_score=round((float(math)+float(science)+float(english))/3, 2)
    row.append(average_score)
    if average_score<60:
        status="Fail"
    else:
        status='Pass'
    row.append(status)
    filtered_data.append(row)

filtered_data.sort(key=lambda x: float(x[4]), reverse=True)
with open(output, 'wt', newline="") as file:
    writer=csv.writer(file)
    writer.writerow(header)
    writer.writerows(filtered_data)
print("Report generated succesfully")








