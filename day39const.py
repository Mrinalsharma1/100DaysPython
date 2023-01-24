class demo:
    def __init__(self,a,b):
        self.name=a
        self.occ=b
        # print("hey")
    def info(self,d):
        print(f"{self.name} is a {self.occ} value is {d}")
    def check(self,x):
        x.info(5)
        
        
obj=demo("hello","Hr") #when object created constructor will automatically called
obj.info(1) #we can pass value into method also
obj.check(obj) #we can pass obj also as a argument

