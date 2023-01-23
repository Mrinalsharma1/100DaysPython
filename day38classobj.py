class demo:
    name="helo"
    course="MCA"
    def info(self): #self represent self references
        print(f"{self.name} is a {self.course}")
obj =demo() #create object in python
obj.info()
# print(obj.course)