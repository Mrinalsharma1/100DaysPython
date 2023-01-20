def add(x,y): #norma function
    return x+y
print(add(6,6))

add= lambda x,y:(x+y) #that is lamda function
print(add(6,6))

avg=lambda x,y,z:(x+y+z)/3
print(int(avg(3,4,5)))

square=lambda x:(x*2)

def square1(square,value):
    return 7+square(value)
print(square1(square,2)) #passing function as a argument

a=lambda x,y:print(f'{x} * {y}= {x*y}')
a(3,4)