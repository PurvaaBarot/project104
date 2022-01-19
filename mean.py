import csv
from statistics import mean

with open("SOCR-HeightWeight (1).csv" , newline="") as f:
    line=csv.reader(f)
    file_data=list(line)

file_data.pop(0)
weight=[]
length=len(file_data)

for i in range(length):
    w=file_data[i][2]
    weight.append(float(w))

total=0
for i in weight:
    total=total+i    

mean=total/length    
print("Mean= ", mean)