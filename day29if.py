a=200
b=3300
# print("A") if a>b else print("=") if a ==b else print("B")

c=9 if a>b else 0
print(c)

# enumerated function 

fruit=['apple','banana','mango']
for i, f in enumerate(fruit): #it will start from zero if u want to set the start value we can pass (fruit , start=1) start argument
    print(f" index is : {i} & name is : {f} ")
