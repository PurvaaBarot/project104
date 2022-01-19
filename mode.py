import csv
from collections import Counter

with open("SOCR-HeightWeight (1).csv" , newline="") as f:
    line=csv.reader(f)
    file_data=list(line)

file_data.pop(0)
weight=[]
length=len(file_data)

for i in range(length):
    w=file_data[i][2]
    weight.append(float(w))

counts=Counter(weight)

valueCount=list(counts.values())    

max=max(valueCount)
print(max)

keys=list(counts.keys())

maxindex=valueCount.index(max)

mode=keys[maxindex]
print(mode)

