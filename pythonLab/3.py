# Program to Find  type of triangle as equilateral(all sides equal), isosceles (two sides the same), or scalene (all sides different).
# a=int(input("enter a side-1:"))
# b=int(input("enter a side-2:"))
# c=int(input("enter a side-3:"))

# if a==b==c:
#     print('equilateral')
# elif (a==b)or(b==c)or(a==c):
#     print('isosceles')
# else:
#     print('scalene')

a=int(input("enter a side -1 : "))
b=int(input("enter b side -2 : "))
c=int(input("enter c side -3 : "))

if a==b==c:
    print("equalitral")
elif(a==b)or (b==c)or(c==a):
    print("isosales")
else:
    print("scalen")