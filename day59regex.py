import re
str="rain is strom rain rain"
# print(re.search('^rain',str))
# print(re.search('strom$',str))
def check(val,pos):
    if val=="rain" :
        return pos
    # helo
    else:
        return 0
data=str.split(' ')
pos=1
for x in data:
    ret=check(x,pos)
    if ret>0:
       print(f"found at position {ret-1}")
    pos+=1
    

