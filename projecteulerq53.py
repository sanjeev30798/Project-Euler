import math
c=0
for i in range(1,101):
    for j in range(1,i+1):
        r=math.factorial(i-j)
        n=math.factorial(i)
        k=math.factorial(j)
        if((n/(r*k))>10**6):
            c+=1
        
print(c)            