#include <bits/stdc++.h>
using namespace std;

void merge(int arr[], int l, int mid, int r)
{
    vector<int> tmp;
    // Your code here
    int left = l;
    int right = mid + 1;
    while (left <= mid && right <= r)
    {
        if (arr[left] <= arr[right])
        {
            tmp.push_back(arr[left]);
            left++;
        }
        else
        {
            tmp.push_back(arr[right]);
            right++;
        }
    }

    // Copy remaining elements
    while (left <= mid)
    {
        tmp.push_back(arr[left]);
        left++;
    }
    while (right <= r)
    {
        tmp.push_back(arr[right]);
        right++;
    }

    for (int i = l; i <= r; i++)
    {
        arr[i] = tmp[i - l];
    }
}

void mergeSort(int arr[], int l, int r)
{
    // code here
    if (l == r)
        return;
    int mid = (l + r) / 2;

    mergeSort(arr, l, mid);
    mergeSort(arr, mid + 1, r);

    merge(arr, l, mid, r);
}

int main()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    mergeSort(arr, 0, n);
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";

    return 0;
}