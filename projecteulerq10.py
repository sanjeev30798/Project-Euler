sum=0
for i in range(2,2000000):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if(count==2):
        sum+=i
    print(i,sum)
print(sum)