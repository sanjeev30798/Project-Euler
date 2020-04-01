sum1=0
h=10**10
for i in range(1,1000):
    print(i)
    sum1=(sum1%h+pow(i,i,h)%h)%h
print(sum1)    