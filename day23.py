#docString in python
def square(n):
    '''this is docstring in python'''
    print (n**2)
square(5)
print(square.__doc__)#it will display the docstring 

#factorial in python
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

#febonacci series
def febo(n):
    if(n<=1):
        return n
    else:
        return febo(n-1)+febo(n-2)
n=6
if n<= 0:
    print("number is less than zero")
else:
    for i in range(n):
        print(febo(i))