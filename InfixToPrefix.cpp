#include <bits/stdc++.h>
using namespace std;
int Precedence(char c)
{
    if (c == '^')
        return 3;
    else if (c == '*' || c == '/')
        return 2;
    else if (c == '+' || c == '-')
        return 1;
    else
        return -1;
}

string InfixToPrefix(string s)
{
    reverse(s.begin(), s.end());
    stack<char> st;
    string res = "";
    for (int i = 0; i < s.length(); i++)
    {
        /*
        Since the expression is reversed so brackets have been reversed,
        so we gotta add bracket condition by flipping backets in the if-else condtions.
        */
        if ((s[i] >= 'a' && s[i] <= 'z') || s[i] >= 'A' && s[i] <= 'Z')
            res += s[i];
        else if (s[i] == ')')
            st.push(s[i]);
        else if (s[i] == '(')
        {
            while (!st.empty() && st.top() != ')')
            {
                res += st.top();
                st.pop();
            }
            if (!st.empty())
                st.pop();
        }
        else
        {
            while (!st.empty() && (Precedence(st.top()) >= Precedence(s[i])))
            {
                res += st.top();
                st.pop();
            }
            st.push(s[i]);
        }
    }
    while (!st.empty())
    {
        res += st.top();
        st.pop();
    }
    reverse(res.begin(), res.end());
    return res;
}

int main()
{
    string s = "(a-b/c)*(a/k-l)";
    cout << InfixToPrefix(s) << endl;
    return 0;
}
