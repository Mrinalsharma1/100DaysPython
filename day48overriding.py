class demo:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
class circle(demo):
    def __init__(self, radious):
        self.radious=radious
        super().__init__(radious,radious)
    def area(self):
        return 3.14*super().area() 
obj=demo(5,4)
print(obj.area())
cir=circle(6)
print(cir.area())
