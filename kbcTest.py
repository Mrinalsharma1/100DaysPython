question=[
    ["which language was used in Fb?","react","java","javascript","None"],
    ["which language was used in whatsApp?","typescript","java","javascript","None"],
    ["which language was used in Twitter?","Angular","java","javascript","None"],
]
queans=["react","typescript","angular"]
userans=[]
for i in question:
    temp=len(i)-1
    for j in range(0,temp):
        print(i[j])   
    a=input("Enter your Answer : ")
    userans.append(a)
ans=0
wrong=0
print(userans)
for j in range(0,len(userans)):
    if(userans[j].casefold()==queans[j]):
        ans+=1
    else:
        wrong+=1
print(f"correct answer is {ans} and wrong answer is {wrong} ") 
