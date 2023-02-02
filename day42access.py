class geek:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def dis(self):
        print(f"age is = {self.age}")
        
obj=geek("mrinal",56)
print(obj.name) #public variable can be access
obj.dis()

# snake water gun game
import random
def check(comp,user):
    if comp==user:
        return 0
    if(comp==0 and user==1):
        return -1
    if(comp==1 and user==2):
        return -1
    if(comp==2 and user==0):
        return -1
    return 1
comp=random.randint(0,2)
user=int(input("0 for snake, 1 for water and 2 for gun : "))

print("You chose :",user)
print("computer chose :",comp)

score=check(comp,user)
if(score==0):
    print("it's a draw")
elif(score==-1):
    print("You Lose")
else:
    print("You Won")
