print("-----------Day19----------")
l=[2,4,5,6,7,8,2,3,0]
print(l)
l.append(5)#it's append the element in the last
l.sort(reverse=True)#it's reverse the value in desending order
l.reverse()#it's just reverse the origin list
print(l)
print(l.index(2))
print(l.count(3))
m=l.copy()#copy the the list
m[0]=0
l.insert(1,256)#insert value at specific position
k=l+m #add two list
print(k)
print(m)
print(l)
