def searchInSorted(self,arr, k):
    for n in arr:
        if(n == k):
            return True
        elif (n > k):
            break
    return False