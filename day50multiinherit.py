class emp:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"emp name is {self.name}")
        
class dance:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"dance type is {self.dance}")
        
class emptype(emp,dance): #multiple inheritance
    def __init__(self,name,dance): #here if we change the order then the class show method will also change
        self.dance=dance
        self.name=name
        
obj=emptype('nittu',"kathak")
print(obj.name)
print(obj.dance)
obj.show()
print(emptype.mro()) #it will show the flow of class object. which show will call first