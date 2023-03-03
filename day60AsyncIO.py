import time
import asyncio
import requests

# below code is working synchronously (line by line)
# def fun1():
#     print("fun1")
#     time.sleep(2)
# def fun2():
#     print("fun2")
#     time.sleep(2)
# def fun3():
#     print("fun3")
#     time.sleep(2)
    
# fun1()
# fun2()
# fun3()

async def fun1():
   
    URL = "https://images.pexels.com/photos/1420440/pexels-photo-1420440.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
    response = requests.get(URL)
    open("img1.jpg", "wb").write(response.content)
    print("fun1")
    return "img1"
async def fun2():
    URL = "https://images.pexels.com/photos/259915/pexels-photo-259915.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
    response = requests.get(URL)
    open("img2.jpg", "wb").write(response.content)
    print("fun2")
    return "img2"
async def fun3():
    URL = "https://plus.unsplash.com/premium_photo-1668241683684-c65571f89df2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80"
    response = requests.get(URL)
    open("img3.jpg", "wb").write(response.content)
    print("fun3")
    return "img3"
    
async def main():
    l=await asyncio.gather( #with this we can execute our task parlell
        fun1(),
        fun2(),
        fun3()
    )
    print(l)
    # task=asyncio.create_task(fun1())
    # await fun1()
    # await fun2()
    # await fun3()
asyncio.run(main())#here we are giveing istruction to this main function to run all the function