import time
t=time.localtime()
ct=int(time.strftime("%H",t))
# print(type(ct))

if(ct>4 and ct<12):
    print("Good Morning Sir ")
elif(ct>12 and ct<16):
    print("Good Afternoon Sir ")
elif(ct>16 and ct<20):
    print("Good Evening Sir ")
else:
    print("Good Night Sir ")

