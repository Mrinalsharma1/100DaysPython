print("--------day4---------")
a=int(input("Enter first Element "))
b=int(input("Enter second Element "))
print("1. Add")
print("2. Sub")
print("3. MUl")
print("4. Div")
ch=int(input("Enter Your Choise "))
if ch==1:
    print("sum of",a,"and", b,"is =",a+b)
elif ch==2:
    print("sub of",a, "and", b,"is =",a-b)
elif ch==3:
    print("mul of", a, "and", b, "is =",a*b)
else:
    print("div of ",a, "and", b," is ",a/b)
    
