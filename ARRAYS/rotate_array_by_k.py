def rotateByk(nums, k):
    def reverse(arr, s, e):
        while s < e:
            arr[s], arr[e] = arr[e], arr[s]
            s, e = s+1, e-1
    
    n = len(nums)
    k = k%n
    
    reverse(nums, 0, n-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)