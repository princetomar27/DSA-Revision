#include <bits/stdc++.h>
using namespace std;

void revFun(int i, int arr[], int n)
{
    if (i >= n / 2)
    {
        return;
    }
    swap(arr[i], arr[n - i - 1]);
    revFun(i + 1, arr, n);
}

// Check palindrome
void revStr(int i, string &str, int n)
{
    if (i >= n / 2)
        return;
    swap(str[i], str[n - i - 1]);
    revStr(i + 1, str, n);
}

string stringReverse(string str)
{
    string tmp = str;
    revStr(0, tmp, tmp.length());
    return tmp;
}

bool isPalindrome(string s)
{
    string rev = stringReverse(s);
    for (int i = 0; i < s.length(); i++)
    {
        if (rev[i] != s[i])
            return false;
    }

    return true;
}

int main()
{
    string s;
    cout << "str : ";
    cin >> s;
    cout << "\nEntered string : " << s << endl;
    bool palin = isPalindrome(s);

    cout << std::boolalpha;
    cout << "Is String Palindrome: " << palin << endl;
}