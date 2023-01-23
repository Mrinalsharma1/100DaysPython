# diffirent between == and is
a=[12,23,33]
b=[12,23,33]

print(a==b) #it compare value and return true
print(a is b) #it's compare the memory location of both list bcus list is mutable so it return false

a=3
b=3
print(a==b) #it's return true bcus variable is constant
print(a is b) #it's return true bcus variable memory address is same