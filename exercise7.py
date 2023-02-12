import os 
from pathlib import Path
old_file=(f"{os.getcwd()}\demo\check.png")
old_file=r"E:/Mrinal_py/demo/check.png"
print(old_file)
name="1.txt"
new_file=(f"{os.getcwd()}\demo\{name}")
new_file=r"E:/Mrinal_py/demo/1.txt"
print(new_file)
os.rename(old_file,new_file)
# print(curr)

old_name = "100DaysPython/demo/temp.png"
new_name = "100DaysPython/demo/1.png"

# # Renaming the file
path=Path(old_name)
if(path.is_file()):
    os.rename(old_name, new_name)
    print("file exist")
else:
    print("not find")
    
# exercise soluction by codewithharry

files=os.listdir("100DaysPython/demo") #create files in list
i=1
for file in files:
    if file.endswith('.jpg'): #check file is end with .jpg or not
        print(file)
        os.rename(f"100DaysPython/demo/{file}",f"100DaysPython/demo/{i}.jpg") #rename the file 
        i=i+1