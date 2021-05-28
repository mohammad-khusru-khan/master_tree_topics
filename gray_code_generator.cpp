/*
cpp program to generate n-bit gray codes.
vector is the data structure being used to store the gray codes for efficient logic.
*/
#include <bits/stdc++.h>
using namespace std;
void gray_code_generator(int n)
{
    if(n <= 0)
        return;
        
    vector<string> gray;
    gray.push_back("0");
    gray.push_back("1");
    int x, y;
    for (x = 2; x < (1 << n); x = x << 1)
    {
        for (y = x - 1; y >= 0; y--)
            gray.push_back(gray[y]);
        for (y = 0; y < x; y++)
            gray[y] = "0" + gray[y];

        for (y = x; y < 2 * x; y++)
            gray[y] = "1" + gray[y];
    }
    cout<<"The " << n << " bit gray codes are :" << endl;
    for(x = 0; x < gray.size(); x++)
        cout << gray[x] << endl;
}

int main()
{
    int n;
    cout<<"Enter the number of number of bits required for gray codes.: ";
    cin>>n;
    gray_code_generator(n);
    return 0;
}
