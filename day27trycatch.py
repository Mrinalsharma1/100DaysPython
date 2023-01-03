#try catch block
n=input("Enter Number : ")
print(f"Number is {n} ")
try:
    for i in range(1,11):
        print(f"{int(n)} * {i} = {int(n)*i} ")
except Exception as e: #error woude be stored in e
    print(e)
except: #direcr print the msge after any error
    print("something wrong")
    
    
try:
    n=int(input("enter any innteger number : "))
    a=[2,3]
    print(a[6])
except ValueError:
    print("num is not int ",ValueError)
except IndexError:#write multiple except block
    print("index error ")


print("some imp code here")
print("end of the program")