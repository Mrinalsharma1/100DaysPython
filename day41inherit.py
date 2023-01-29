class emp:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def show(self):
        print(f"employee id is {self.id} and name is {self.name} ")
        
class payment(emp): #single inheritance
    lpa=4
    def empdetail(self):
        print(f"emp id is {self.id} and name is {self.name} and LPA is {self.lpa}")
obj=payment(103,"rajan")
obj.show()
obj.empdetail()
