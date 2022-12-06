print("--------day4---------")
print("1. Add")
print("2. Sub")
print("3. MUl")
print("4. Div")

while i==1:
    i=int(input("Do you want to input more for 1 YES 2 For NO "))
    a=int(input("Enter first Element "))
    b=int(input("Enter second Element "))
    ch=int(input("Enter Your Choise "))
    if ch==1:
        print("sum of",a,"and", b,"is =",a+b)
    elif ch==2:
        print("sub of",a, "and", b,"is =",a-b)
    elif ch==3:
        print("mul of", a, "and", b, "is =",a*b)
    else:
        print("div of ",a, "and", b," is ",a/b)
    
