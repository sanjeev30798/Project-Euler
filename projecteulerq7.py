c=0
s=1
while(c<10001):
    count=0
    for i in range (1,s+1):
        if(s%i==0):
            count+=1
    if(count==2):
        c+=1
    print(s,c)
    s+=1
print(s-1)   