f=open('E:/Mrinal_py/100DaysPython/myfile.txt','a')
i=0
while True:
    i+=1
    line=f.readline()
    if not line:
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    print(f"marks of student {i} in maths is : {m1*2}")
    print(f"marks of student {i} in science is : {m2*2}")
    print(f"marks of student {i} in sst is : {m3*2}")
    print(line)

lines=['line 1','line 2','line 3']
for i in lines:
    f.write(i+'\n')
f.close

with open("E:/Mrinal_py/100DaysPython/myfile.txt",'r') as f:
    print(type(f))
    f.seek(10) #it start reading character from 10 position 
    data=f.read(5)#and read after 5 character
    print(data)

with open("E:/Mrinal_py/100DaysPython/myfile.txt",'w') as f:
    f.write("hello world")#it will store this string
    f.truncate(3)# but only till truncated size
with open("E:/Mrinal_py/100DaysPython/myfile.txt",'r') as f:
    print(f.read())