class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k" #print the value
    def __add__(self,a):
        print(a)
        return f"{self.x+a.x}i + {self.y+a.y}j + {self.z+a.z}k" #print two vector object value and return str
    def __add__(self,a):
        return Vector(self.x+a.x,self.y+a.y,self.z+a.z) #print sum of two vector object value and return type will be also vector
    
    # __add__ it is a python + operator overloding
v=Vector(3,4,5)
print(v)

v1=Vector(5,6,9)
print(v+v1)
print(type(v+v1))