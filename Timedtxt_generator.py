import sys,io,random
from time import perf_counter

values=[]
for _ in range(100000):
    value = random.randint(1,100000)
    values.append(str(value))
count =0

start=perf_counter()
file1 = open("myfile1.txt","wt")
for i in range(len(values)):
    file1.write(values[i])
    file1.write('\n')
file1.close()
elapsed = perf_counter()-start
print(F"Done in {elapsed:8.3}");

start=perf_counter()
file1 = open("myfile2.txt","wt")
for i in values:
    file1.write(i)
    file1.write('\n')
file1.close()
elapsed = perf_counter()-start
print(F"Done in {elapsed:8.3}");
