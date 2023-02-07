class parentClass:
    def parent_method(self):
        print("This is the parent methods...")
        
class childClass(parentClass): #inharite parent class
    def parent_method(self):
        print("test")
        super().parent_method()
    def child_method(self):
        print("This is the child methods...")
        super().parent_method() #calling parent class
        
child_object=childClass() #create obj of childclass
child_object.parent_method() #calling parent method

# best example
class customer:
    def __init__(self,id,name):
        self.id=id
        self.name=name
class employee(customer):
    def __init__(self, id, name):
        super().__init__(id, name) #inharite customer class constructor
        self.lang="python"

obj=employee(101,"rohan")
print(obj.name)
print(obj.id)
print(obj.lang)

