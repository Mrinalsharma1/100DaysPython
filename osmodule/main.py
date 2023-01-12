import os
# os.mkdir("data")
if (not os.path.exists("data")):
    os.mkdir("data")
    
os.system(r"E:/Mrinal_py/100DaysPython/osmodule/data/Days1/temp.py")
    
for i in range(0,100):
    if(not f"data/Days {i+1}"):
        os.mkdir(f"data/Days {i+1}")
    elif ( f"data/Days {i+1}"):
        os.remove(f"data/Days {i+1}/myfile.txt",f"data/Days {i+1}/temp.py")
    elif (f"data/Days {i+1}/"=="temp.py"):
        print("heu")
        
    else:
        with open(f"data/Days {i+1}/myfile.txt", 'w') as fp:
            pass
        with open(f"data/Days {i+1}/temp.py", 'w+') as fp:
            pass
