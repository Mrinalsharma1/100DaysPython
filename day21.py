print("-----------Day21----------")
# operation on Tupple
count=("pak","china","india","goa","denmark")
print(count)
print(list(count))#convert tupple into list
temp=list(count)
temp.append("delhi")#add item into list we can not do any operation on tupple
print(temp)
print(temp.pop(2))#delete item base on index
temp[2]="style"
count=tuple(temp)#convert list into tupple
print(count)
test=(1,2,3,3,3,4,5,6,4,4)
print(test.count(3))#it's give the occurance of given item
