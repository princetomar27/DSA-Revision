#include <bits/stdc++.h>
using namespace std;

void bubbleSort(int arr[], int n)
{
    for (int i = n - 1; i >= 0; i--)
    {
        for (int j = 0; j < i; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                // swap
                int t = arr[j + 1];
                arr[j + 1] = arr[j];
                arr[j] = t;
            }
        }
    }
}

int main()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    bubbleSort(arr, n);
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";

    return 0;
}