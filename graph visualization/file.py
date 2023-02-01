f = open("data/data.txt", 'r')
f2=open("data/data-1000.txt",'w')

f_lines=f.readlines()

count=0
for line in f_lines:
    if count>=1000: break
    f2.write(line)
    count+=1
    
print("complete")

f.close()
f2.close()
