class demo:
    sallary=0 #class variable
    def __init__(self,name):
        self.name=name #instance variable
        
    def show(self,sal):
        age=0
        print(f"name is : {self.name} and salary is : {self.sallary+sal} & age is : {age} ")
        
        # print(self.num)
obj=demo(7)
obj.sallary=2000 #updating class variable
# obj.show.age=34 #we can not update variable from here
obj.show(4000)

