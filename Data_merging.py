import csv
import pandas as pd

file1 = 'data(127).csv'
file2 = 'data(128).csv'

d1 = []
d2 = []
with open(file1,'r',encoding='utf8') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        d1.append(i)
        
with open(file2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]

pog1 = d1[1:]
pog2 = d2[1:]

h = h1+h2

p_d =[]

for i in pog1:
    p_d.append(i)
for j in pog2:
    p_d.append(j)
with open("Data_merged.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(p_d)
    
df = pd.read_csv('Data_merged.csv')
df.tail(8)
print('Your both files merged sucessfully')