from functools import lru_cache
import time

@lru_cache(maxsize=None) #it provide us a cache memory for repeted work
def fx(n):
    time.sleep(5)
    return n*5
print(fx(20))
print("done foe 20 sec")
print(fx(10))
print("done foe 10 sec")
print(fx(5))
print("done foe 5 sec") #till here for every call it will take 5sec

print(fx(20)) #from here it's all ready calculated so it wont take time
print("done for 20 sec")
print(fx(10))
print("done for 10 sec")
print(fx(5))
print("done for 5 sec")