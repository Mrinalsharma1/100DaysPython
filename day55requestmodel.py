import requests
from bs4 import BeautifulSoup

# res=requests.get("https://www.codewithharry.com") #get data from this url
# print(res.text) #print the code of this url

url1="https://alphaworldtech.com"
r=requests.get(url1)
#test purpose
soup=BeautifulSoup(r.text,'html.parser') #it is used the scrape the data from web
# print(soup.prettify())
for heading in soup.find_all('p'): #here we are finding the data from p tag
    print(heading.text) #printing the data from p tag

# url="https://jsonplaceholder.typicode.com/posts"
# data={
#     "title":'foo',
#     "body":'bar',
#     'userId':1,
# }
# headers={
#     'Content-type':'application/json; charset=UTF-8'
# }
# resp=requests.post(url,headers=headers,json=data) #get request