def isSortedAndRotated(nums):
    # get the length of nums
    n = len(nums)
    cnt = 0

    # count the number of elements greater than next element
    for i in range(n):
        if nums[i] > nums[(i+1) % n]:
            cnt += 1
    return cnt <= 1

def isSortedAndRotatedBest(nums):
    n = len(nums)
    violations = 0
    for i in range(n):
        if nums[i] > nums[(i+1) % n]:
            violations += 1
            if violations > 1:
                return False
    return True

if __name__ == '__main__':
    arr = [3, 4, 5,1, 2]
    n = len(arr)
    if isSortedAndRotatedBest(arr):
        print("Array is sorted")
    else:
        print("Array is not sorted")