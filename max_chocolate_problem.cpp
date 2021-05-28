#include <bits/stdc++.h>
using namespace std;
/*
Each Chocolate is of one rupee, 3 wrappers can get you one chocolate.
what is the maximum number of chocolate one can buy
*/

int max_chocolates(int n)
{
    int wrappers = 0, chocolates = 0;
    //We'll buy all the chocolates with all the money,so both become n
    wrappers = n; chocolates = n;
    while (wrappers > 1)
    {
        /*
        we calculate the  current number of wrappers.
        deduct the used wrappers and buy new chocolates with them.
        both chocolates and wrappers are updated with new number of new chocolates bought.
        */
        int new_chocolates = int(wrappers / 3);
        wrappers -= new_chocolates * 3;
        chocolates += new_chocolates;
        wrappers += new_chocolates;
    }
    return chocolates; 
}

int main()
{
    int n;
    cout << "Each chocolate is worth a rupee.\nEnter the amount. :";
    cin>>n;
    cout << "We can buy " << max_chocolates(n) << " chocolates with " << n << " rupees.";
}

// Use sample input as n = 15
