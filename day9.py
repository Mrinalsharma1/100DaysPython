print("-----------Day9----------")
#string are immutable
a="harry!!! hsghd shgdhs !!"
print(len(a))
print(a.upper())#to print upper case
print(a.lower())#to print lower case
print(a.rstrip("!"))#to delete ! from string
print(a.replace("harry","shyam"))#to replace string
print(a.split(" ")) #split with space 
blog="this is react"#this iS NAMe
print(blog.capitalize())#to captilize first char
print(blog.center(50))#it center the string 
print(a.count("harry"))#check how many time this value is exist in a
print(a.endswith("!!"))#if it's exist then return true
print(a.endswith("to",0,5))#if to is exist b/w 0 to 5 then true else false
print(blog.find("is")) #it's count how many times is exist
print(blog.swapcase())#convert upper to lower and lower to upper
print(blog.title()) #to make first string of char capital

