#include<bits/stdc++.h>
using namespace std;
int main()
{
    int s=0,count=0,i,j=1;
    while(1)
    {
        count=0;
        s=s+j;
        for(i=1;i<=sqrt(s);i++)
        {
            if(s%i==0)
            {
                if(s/i==i)
                    count++;
                else
                    count+=2;
            }
        }
        if(count>500)
            break;
        j++;

    }
    cout<<s;
}
