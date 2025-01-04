def findUnion(a,b):
    # code here 
    out = []
    i,j =0,0
    m = len(a)
    n = len(b)
    current = 0
    
    while (i < m and j < n):
        if (a[i] == b[j]):
            out.insert(current, a[i])
            i+=1
            j+=1
            current+=1
        else:
            if(a[i] < b[j]):
                out.insert(current, a[i])
                i += 1
                current += 1
            else:
                out.insert(current, b[i])
                j += 1
                current += 1
    
    while i < m:
        if i == 0 or a[i] != a[i-1]:
            out.insert(current, a[i])
            i += 1
            current += 1
    while j < n:
        if j == 0 or b[j]!= b[j-1]:
            out.insert(current, b[j])
            j += 1
            current += 1

    return out
            

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 6, 7]
    
    print(findUnion(a, b))