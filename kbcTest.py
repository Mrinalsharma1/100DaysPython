question=[
    ["which language was used in Fb?","react","java","javascript","None","react"],
    # ["which language was used in whatsApp?","typescript","java","javascript","None","typescript"],
    # ["which language was used in Twitter?","Angular","java","javascript","None","angular"],
]
queans=[]
userans=[]
# print(type(userans))
# a=(question[0])
# print(a[0])
for i in question:
    temp=len(i)-1
    for j in range(0,temp):
        if (j==0):
            queans.insert(0,j)
        print(i[j])
        
    ans=input("Enter your Answer : ")
    userans.insert(0,ans)
print(userans)   
print(queans)   
