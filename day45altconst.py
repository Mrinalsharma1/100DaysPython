class demo:
    def __init__(self,name,sallary):
        self.name=name
        self.sal=sallary
    @classmethod
    def fromstr(cls,str): #this is alternate constructor
        name,sal=str.split("-")
        return cls(name,int(sal))
        
obj=demo("mrinal",23000)
print(obj.name)
print(obj.sal)
str="mrinal-12000" #what if data is in form of string
res=obj.fromstr(str)
print(res.name)
print(res.sal)
temp=str.split("-")
# print(temp[0],temp[1]) #here we will get data but to avoid to write code in main we will create alternate constructor

# dir,__dict__,help method in python \/

a=[1,2,3]
print(type(a))
print(dir(a)) #it will display the list of predefine methods

print(obj.__dict__) #it will display the object related info like constructor

print(help(obj)) #it will give the documantation view of object