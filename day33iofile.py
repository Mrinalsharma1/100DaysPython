x=5
def demo():
    global y #to make variable global use global keyword
    y=7
    print(y+x)
demo()
print(y)

# f = open("E:/Mrinal_py/100DaysPython/myfile.txt", "a")
# # print(f)
# text=f.read() #to read the content in the file
# print(f)
# f.close()  

f = open("E:/Mrinal_py/100DaysPython/myfile.txt", "a")
# print(f)
f.write("hello, world") #to read the content in the file
f.close()   

with open("E:/Mrinal_py/100DaysPython/myfile.txt", "a") as f:
    f.write("my name is raj!")