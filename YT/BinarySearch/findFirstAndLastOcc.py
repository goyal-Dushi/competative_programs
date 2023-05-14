# We need to return an index arr of size 2 containing the index of first
# and last occurence of an element in the sorted arr
# arr may or may not have duplicates 

# GIVEN : sorted arr and Target

# TC log(n) , SC log(n)
# recursive fn to find first occurence of a num in sorted arr
def firstOcc(arr, target, strt, end, fo):
    if(strt > end):
        return fo
    
    mid = strt + (end-strt)//2
    if(arr[mid] == target):
        fo = mid
        return firstOcc(arr, target, strt, end-1, fo)
    elif(arr[mid] > target):
        return firstOcc(arr, target, strt, end-1, fo)
    else:
        return firstOcc(arr, target, strt+1, end, fo)

# TC log(n) , SC log(n)
# recursive fn to find last occurence of a num in sorted arr 
def lastOcc(arr, target, strt, end, lo):
    if(strt > end):
        return lo
    
    mid = strt + (end-strt)//2
    if(arr[mid] == target):
        lo = mid
        return lastOcc(arr, target, mid+1, end, lo)
    elif(arr[mid] > target):
        return lastOcc(arr, target, strt, mid-1, lo)
    else:
        return lastOcc(arr, target, mid+1, end, lo)

# overall TC : log(n) (of fo) + log(n) (of lo) , SC : log(n) + log(n)
def firstAndLastOcc(arr, target):
    
    len_arr = len(arr)
    fo = firstOcc(arr, target, 0, len_arr-1, -1)
    lo = lastOcc(arr, target, 0, len_arr-1, -1)
    return [fo, lo]

arr = [5,7,7,8,8,8,8,10]
print(firstAndLastOcc(arr, 7))