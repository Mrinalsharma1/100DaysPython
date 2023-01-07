import random
import string
key1="hello"
if (len(key1)>=3):
    f=key1[0]
    sli= key1[1: ]
    sli+=f
    res = ''.join(random.choices(string.ascii_letters, k=3))
    sli+=res
    res+=sli
    print("Secret Password : ",res)
else:
    print("Secret Password : ",key1[::-1])