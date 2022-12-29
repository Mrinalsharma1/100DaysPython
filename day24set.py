#set in python
# s={2,3,4,5,4}
# print(type(s))#it will print set
# s1={"hey",5,7.7,5.0}
# print(s1)#here it will not print 5.0
# for i in s1:
#     print(i) #print value of the set
    
#to define blank set we have to use set method
s=set()
print(type(s))

s1={1,3,2,4,3,2,7,5}
s2={3,4,5,7,3}
print(s1.union(s2))#in this the original set will be not updated
# s1.update(s2)#original set will be updated s1
# print(s1)
# print(s1.intersection(s2))#in both set value shoude be common
# print(s1.symmetric_difference(s2))#all value will be display accept common value
# print(s1.difference(s2))#value which is uniqely exist in s1 will be display
# print(s1.isdisjoint(s2))#if both set is unique then return true or else false
# print(s1.issuperset(s2))#if the s2 all value is exist in s1 then return true else false
s2.add(9)#to add value in the set
print(s2)
s3={0,9,8,7}
s2.update(s3)#to add multiple value in the set
print(s2)
# s2.remove(11)#to remove the item from set if value not match the through error
# print(s2)
s2.discard(11)#it will not through any error if value is not exist in the set
print(s2)
print(s2.pop())#get any one value from set
# del s2 #it will delete set
print(s2)
s2.clear #it will just remove the value of the set
print(s2)

