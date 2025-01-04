def getNumberAppearsOnce(arr):
    res = 0
    for x in range(len(arr)):
        res ^= arr[x]
    
    return res

if __name__ == '__main__':
    arr = [0,1,0,3,1,3,2,2,4,5,5]
    n = len(arr)
    print(arr)
    print(getNumberAppearsOnce(arr))
    print(arr)