i=143
s1=set()
s2=set()
s3=set()
while(True):
    a=i*(i+1)//2
    b=i*(3*i-1)//2
    c=i*(2*i-1)
    s1.add(a)
    s2.add(b)
    s3.add(c)
    if(a in s2 and a in s3 and a!=40755):
        print(a)
        break
    i+=1
    
## answer is 1533776805 