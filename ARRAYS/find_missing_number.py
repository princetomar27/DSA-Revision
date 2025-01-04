def findMissingBruteForce(nums):
    n = len(nums)
    num_set = set(range(n + 1))  

    for num in nums:
        num_set.remove(num)  

    return num_set.pop() 

def findMissingOptimised(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2  
    actual_sum = sum(nums)  
    return expected_sum - actual_sum

if __name__ == '__main__':
    a = [0,1, 2, 4, 5]
    
    print(findMissingBruteForce(a))
    print(findMissingOptimised(a))