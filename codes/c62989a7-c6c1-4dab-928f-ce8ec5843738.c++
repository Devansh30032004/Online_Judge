#include <bits/stdc++.h>
using namespace std;

#define ll long long int 

int main()
{
    int n, a;
    cin >> n;

    int stud[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a;
        stud[i] = a;
    }

for (int i = 0; i < n; i++)
{
    for (int j = i+1; j < n; j++)
    {
        if (stud[i]==stud[j]&&stud[j]!=0)
        {
            stud[j] = 0;
        }
        
    }
    
}

    int oppai[n],p=0;
    for (int i = 0; i < n; i++)
    {
        if (stud[i]!=0)
        {
            oppai[p] = stud[i];
            p++;
        }
        
    }
    cout << p+1;

    return 0;
}