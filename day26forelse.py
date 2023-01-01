#for in if_else 
for i in range(6):
    print(i)
else:
    print("not exist") #here else will execute

for i in range(6):
    print(i)
    if i==4:
        break #else will not execute
else:
    print("not exist")

#in while case
i=0
while i<7:
    print(i)
    if i==4:
        break
    i=i+1
else:
    print("not execute")