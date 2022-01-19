import csv
from statistics import median

with open("SOCR-HeightWeight (1).csv" , newline="") as f:
    line=csv.reader(f)
    file_data=list(line)

file_data.pop(0)
weight=[]
length=len(file_data)

for i in range(length):
    w=file_data[i][2]
    weight.append(float(w))

weight.sort()

if length%2==0 :
    m1=float(weight[length//2])
    m2=float(weight[length//2-1])
    median=(m1+m2)/2

else:
    median=float(weight[length//2])

print("median= " , median)        
