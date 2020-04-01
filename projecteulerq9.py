for i in range(1,1000):
    for j in range(i,1000):
        k=j+i
        m=pow(i**2+j**2,0.5)
        if(k+m==1000 and (i*i+j*j==m*m)):
            print(i*j*m)
            print(i,i*i)
            print(j,j*j)
            print(m,m*m)