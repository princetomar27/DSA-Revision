#include <bits/stdc++.h>
using namespace std;

void fun(int i, int n)
{

    // BASE CASE
    if (i >= n)
        return;
    cout << "Hey Prince\n " << i + 1;
    fun(i + 1, n);
}

void parameterSum(int i, int sum)
{
    if (i < 1)
    {
        cout << "Sum : " << sum;
        return;
    }
    parameterSum(i - 1, sum + i);
}

int funSum(int n)
{
    if (n < 0)
    {
        return 0;
    }
    return n + funSum(n - 1);
}

int main()
{
    int n;
    cout << "Enter n : ";
    cin >> n;
    parameterSum(n, 0);
    cout << "\nFunctional sum : " << funSum(n);
}