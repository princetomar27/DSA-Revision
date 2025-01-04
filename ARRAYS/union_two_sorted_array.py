#Function to return a list containing the union of the two arrays.
def findUnion(self,a,b):
    # code here 
    res = []
    i,j = 0,0
    m,n = len(a), len(b)

    while i < m and j < n:
        # skip in array a if items are duplicate
        if i>0 and a[i-1] == a[i]:
            i+=1
            continue
        # skip in array b if items are duplicate [if current is same as previous element]
        if j > 0 and b[j-1] == b[j]:
            j += 1
            continue
        
        # compare a[i] and b[j]
        if(a[i] < b[j]):
            res.append(a[i])
            i += 1
        elif(a[i] > b[j]):
            res.append(b[j])
            j += 1
        else:
            res.append(a[i])
            i += 1
            j += 1
    
    while i < m:
        if i >0 and a[i-1] == a[i]:
            i += 1
            continue
        res.append(a[i])
        i+=1
    
    while j < n:
        if j > 0 and b[j-1] == b[j]:
            j += 1
            continue
        res.append(b[j])
        j+=1
    
    return res
        