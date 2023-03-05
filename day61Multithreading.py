import time
import threading

def fun(sec):
    print(f"sleeping for {sec} seconds")
    time.sleep(sec)
  
time1=time.perf_counter()
# normal call  
# fun(5)
# fun(4)
# time2=time.perf_counter()
# print(time2-time1)

# using threading
t1=threading.Thread(target=fun,args=[3])
t2=threading.Thread(target=fun,args=[7])
t1.start()
t2.start()
t1.join() #it will stop till complete of t1 process
t2.join()
# calculating time
time2=time.perf_counter()
print(time2-time1)