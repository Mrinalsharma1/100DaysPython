class demo:
    def __init__(self,name):
        self.name=name
    
    # name="mrinal"
    def __len__(self):
        i=0
        for c in self.name:
            i+=1
        return i
    def __str__(self):
        return f"name is {self.name}"
obj=demo("mrinals")
print(obj)
# print(obj.__len__())
print(len(obj))