print("-----------Day17----------")
# default argument ex
# def avg(a=6,b=8): #default value if we don't pass any paramete
#     print("Avg of Two Num is : ",(a+b)/2)
# avg(4,5)#parameter

# keyword argument
# def just(fname="raju",lname="kumar",pin=123):
#     print(fname,lname,pin)
# just(pin=123,lname="yadav",fname="raju")#we can change the parameter sequence

# keyword arbitrary keyword
def avg(*num):#it take n num argument
    # print(type(num))
    sum=0
    for i in num:
        sum=sum+i
    print("avg of numb is : ",sum/len(num))
avg(2,4,8)

# key value argument
def demo(**num):
    print(num["f"],num["l"])
demo(f="shyam",l="yadav")