def removeDuplicates(self, arr):
    #Code Here
    unique = 0
    n = len(arr)
    
    for i in range(n):
        if(arr[i] != arr[unique]):
            unique += 1
            arr[unique] = arr[i]
    return unique+1
                