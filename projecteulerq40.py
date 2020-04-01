s="."
for i in range(1,10**6+1):
    s=s+str(i)
sum=1
print(s[10**6])
print(int(s[10])*int(s[1])*int(s[100])*int(s[1000])*int(s[10000])*int(s[10**5])*int(s[10**6]))

# answer is 210