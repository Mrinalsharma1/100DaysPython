import time
import threading
from sys import exit
t=time.localtime()
ftime=time.strftime('%Y-%m-%d %H:%M:%S')
ftime1=time.strftime('%H:%M:%S')
print("Current Time is : ",ftime)
print(ftime1)
temp="20:46:10"

    
def printit(self):
    threading.Timer(1.0, printit).start()
    ftime1=time.strftime('%H:%M:%S')
    print(ftime1)
    if(ftime1==temp):
        return 1
        # print("alarm start")
        # return 0

res=printit()
if(res==1):
    print("alarm start")