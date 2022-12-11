print("-----------Day10----------")
#if else
n=int(input("Enter Number : "))
if(n<18):
    print("You can't Drive")
else:
    print("you can drive")

#if elif else
n=int(input("Enter Number : "))
if(n<0):
    print("number is -ve ",n)
elif(n==0):
    print("number is zero ",n)
else:
    print("number is +ve ",n)
    
#nested if else

n=int(input("Enter Number : "))
if(n>0):
    print("-ve Number")
    if(n>=0 and n<=10):
        print("Number between 0 - 10")
    elif(n>10 and n<20):
        print("Number between 11 - 19")
    else:
        print("Number")
else:
    print("Number >0 ")