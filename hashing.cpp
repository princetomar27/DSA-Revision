#include <bits/stdc++.h>
using namespace std;

void printCnt(int arr[], int n)
{
    map<int, int> mapp;
    for (int i = 0; i < n; i++)
        mapp[arr[i]] += 1;

    int x;
    cin >> x;

    for (int i = 0; i < x; i++)
    {
        int num;
        cin >> num;
        cout << mapp[num] << endl;
    }
}

int main()
{

    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    printCnt(arr, n);

    return 0;
}