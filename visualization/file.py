import csv


f = open("graph visualization/data/data.txt", 'r')
f2=open("graph visualization/data/data-1000.csv",'w',newline='')

f_lines=f.readlines()

wr=csv.writer(f2)
wr.writerow(["source","target","unixtime"])
count=0
for line in f_lines:
    if count>=1000: break
    
    data=line.split(sep=' ')
    
    
    wr.writerow([data[0],data[1],data[2]])
    count+=1
    
print("complete")

f.close()
f2.close()
