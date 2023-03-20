# 7. Creating Functions : Program to generate nth Fib number: 
# def fib(n):
#     if n==0: return 0
#     elif n==1: return 1
#     else: return fib(n-1)+fib(n-2)


# n=int(input("Enter Number : "))
# print(fib(n))

def fib(n):
    if n==0: return 0
    elif n==1: return 1
    else: return fib(n-1)+fib(n-2)

n=int(input("enter any number : "))
for i in range(0,n):
    # print(i)
    print(fib(i))