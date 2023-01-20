cube=lambda a:(a*a*a)
l=[1,1,2,3,4,5]
newl=[]
# for item in l:
#     newl.append(cube(item))
# print(newl) #without map we can cube the list item

# newl=list(map(cube,l)) #with map we are doing same job
print(list(map(cube,l))) #we can write in one line also

#filter
def filter_fun(a): #we can write filter with this way
    return a>2
f=lambda a:a>2 # we can use lamda function to do same things
ne=list(filter(f,l)) #function inside function pasing
# print(ne)

#we can do same filter in one line also
print(list(filter(lambda a:a>2,l)))