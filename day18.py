print("-----------Day18----------")
li=[1,3,4,"raj",8,7,5]#we can store multiple variable in list
if "raj" in li:
    print("yes")
else:
    print("no")
print(li[0:len(li):2])#it's called jump index after each 2 step value will print

li=[i for i in range(4)]#expression inside list
print(li)

lis=[i*i for i in range(8) if i%2==0]
print(lis)