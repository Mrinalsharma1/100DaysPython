#finally keyword in python
def text():
    try:
        l=[2,4,5,6]
        n=int(input("Enter Index : "))
        print(l[n])
        return 1

    except:
        print("something wrong")
        return 0

    finally: #it will always run
        print("Always Run")
res=text()
print(res)

#raise in python
a=int(input("Enter value b/w 5 to 9 : "))
if(a<5 or a>9):
    raise ValueError("value shoude be between 5 to 9")

a=input("Enter something ")
if(a=='quick'):
    pass
else:
    raise ValueError("Error exist")