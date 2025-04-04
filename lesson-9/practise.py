import csv
input=r"D:\MAAB academy new\python\notesforpython\lesson-9\sales_data.csv"
output=r"D:\MAAB academy new\python\notesforpython\lesson-9\sales_report.csv"
#Reading the date
with open(input, 'rt') as file:
    reader=csv.reader(file)
    header=next(reader)
    data=list(reader)

header.append("Total cost")
filtered_data=[]

#Calculating total costs

for row in data:
    quantity=row[2]
    price=row[3]
    total_sales=float(quantity)*float(price)
    row.append(total_sales)

with open(output, 'w', newline="") as file:
    writer=csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)