print(bin(585))
sum1=0
for i in range(1,1000000):
    r=str(i)
    h=bin(i)
    h=h[2:]
    if(r==r[::-1] and h==h[::-1]):
        sum1+=i
print(sum1)        
        