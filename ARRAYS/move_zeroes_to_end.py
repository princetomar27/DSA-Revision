def moveZeroes(nums):
    n = len(nums)
    # lastZero = 0

    # for i in range(n):
    #     if nums[i] != 0:
    #         nums[i], nums[lastZero] = nums[lastZero], nums[i]
    #         lastZero += 1

    i,j =0,0
    while j < n:
        if(nums[j] == 0):
            j += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1



if __name__ == '__main__':
    arr = [0,1,0,3,12]
    n = len(arr)
    print(arr)
    moveZeroes(arr)
    print(arr)
 