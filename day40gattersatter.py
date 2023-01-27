class demo:
    def __init__(self,x):
        self.value=x
        
    def show(self):
        print(f"value is {self.value}")
        
    @property #it's shows you are return some value
    def gett(self): #setter to set the value and return the updated value
        return 10*self.value
    
    def sett(self,y): #getter to update the value
        self.value=y
obj=demo(10)
obj.show()
obj.sett(5)
print(obj.gett)
# obj.gett()