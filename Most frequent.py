str=(input("enter a string:"))
count={}
for x in str:
    if x in count.keys():
        count[x]+=1
    else:
        count[x]=1 
sort=sorted(count.items(),key=lambda x:x[1],reverse=True)     
print(x,"=",sort[x])
