class emp:
    empcount=0
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
        emp.empcount+=1
    
    def countemp(self):
        print(f"no of employee {emp.empcount}")
        
    def displayemp(self):
        print(f"emp name is {self.name} and emp sal is {self.sal} ")
        
obj1=emp("rana","10000")
obj1.countemp()
obj1.displayemp()
obj2=emp("nish","30000")
obj2.countemp()
obj2.displayemp()
        
    