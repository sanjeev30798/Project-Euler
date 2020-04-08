max1=1
for i in range(0,100):
    for j in range(0,100):
        str1=str(pow(i,j))
        sum1=0
        for k in str1:
            sum1+=int(k)
        if(sum1>max1):
            max1=sum1
print(max1)
            
        
        