def my_gen():
    for i in range(5):
        yield i #when we call then only it will print
        
obj=my_gen()
print(next(obj)) #with next function we can call multiple time
print(next(obj))

for i in range(4):
    print(next(obj)) #here we can not call in loop it will throw error like StopIteration