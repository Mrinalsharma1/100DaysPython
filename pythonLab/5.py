# 5. Dictionary Program
# dist={"id":"","dag","egg"}
# print(type(dist))
# print(len(dist))
# if "dag" in dist:
#     print("yes")
    
# dist.add("ram")
# print(dist)

# dist.pop()
# print(dist)

dis = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
}
print(len(dis)) # for length
if "model" in dis: # for search
    print("its exist")
dis["color"]="red" #to add
print(dis)
dis.pop("color") # to delete
print(dis)