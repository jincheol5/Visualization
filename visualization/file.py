import csv


f = open("visualization/data/example data.txt", 'r')
f2=open("visualization/data/example data.csv",'w',newline='')

f_lines=f.readlines()

wr=csv.writer(f2)
wr.writerow(["source","target","unixtime"])

for line in f_lines:
    
    data=line.split(sep=' ')
    if line[0]=="source": continue
    
    wr.writerow([data[0],data[1],data[2]])
    
    
print("complete")

f.close()
f2.close()
