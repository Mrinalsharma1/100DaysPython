# 9. Pattern Matching 

# 9.1 Program to match a word at the beginning of a given string

import re
str="rain in spring"
# x=re.search("^rain",str)
# print(x)

# 9.2 Program to match a word at the end of a given string:
print(str.split(" "))
y=re.search("spring$",str)
print(y)