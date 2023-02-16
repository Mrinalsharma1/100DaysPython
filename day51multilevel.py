class detail:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def showdetail(self):
        print(f"name is {self.name} and age is {self.age}")
        
class account(detail):
    def __init__(self,name,sall):
        detail.__init__(self,name,age=23)
        self.sall=sall
    def showdetail(self):
        detail.showdetail(self)
        print(f"sallary is {self.sall}")
        
class emp(account):
    def __init__(self, id,name): #this is constructor
        account.__init__(self,name,sall=4000) #this is the constructor for account class
        self.id=id
    def showdetail(self):
        account.showdetail(self) #here we are invoking account class method
        print(f"emp id is {self.id}")
        
obj=emp(121,"rohan")
obj.showdetail()