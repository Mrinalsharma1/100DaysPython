print("-----------Day15----------")
for i in range(12):
    if(i>=0 or i<5):
        continue
    print("5 x ",i+1," = ",(5*(i+1)))
    i=i+1
        
        
    if (i==10):
        print("skip the line")
        break
    
for i in [2,3,4,5,6,7,8]:
    if(i%2!=0):
        continue
    print(i)
        