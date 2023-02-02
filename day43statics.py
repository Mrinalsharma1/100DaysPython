class demo:
    def __init__(self,x):
        self.v=x
    
    def add(self,a):
        return a+self.v
    
    @staticmethod #static method
    def addtonum(b,c):
        return b+c
    
obj=demo(5)
print(obj.add(5))
print(obj.addtonum(6,5))#static method call
