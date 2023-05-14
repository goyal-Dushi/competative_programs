# FInd the ceil value of a number from the given arr 

# Given : Number, arr 
# To find : ceil value

# iterative method
A = [1,3,4,5,6,7,8,19,23,45,67,83,92]
# TC log(n) , SC O(1)
def ceil(arr, num):
    
    len_arr = len(arr)
    strt = 0
    end = len_arr-1
    ans = 0
    while(strt <= end):
        mid = strt + (end-strt)//2
        
        if(arr[mid] >= num):
            ans = arr[mid]
            end = mid-1
        else:
            strt = mid+1
    
    return ans


print(ceil(A,40))

# recursive method 
# TC log(n) , SC log(n) 
def ceilRecursive(arr, num, strt, end, ceil):
    if(strt > end):
        return ceil
    
    mid = strt + (end-strt)//2

    if(arr[mid] >= num):
        return ceilRecursive(arr, num, strt, mid-1, arr[mid])
    else:
        return ceilRecursive(arr, num, mid+1, end, ceil)

print(ceilRecursive(A, 19, 0, len(A)-1, -1))


# Find ceil of a char, 
# given a sorted char arr, and a target char, we need to find the ceil of that char 
# eg : arr = ['c', 'i', 'g'] , target: 'a' , then , ans = 'c'
# also, they are in rotation , ie, if target: 'z', then, ans  = 'c'

def charCeil(arr, char, strt , end, ans):
    if(strt > end):
        # since arr in rotn, thus, for char if no ceil exists
        # then , we return the first char of arr
        return arr[0]
    
    mid = strt + (end-strt)//2
    if(ord(arr[mid]) >= ord(char)):
        ans = arr[mid]
        return charCeil(arr, char, strt, end-1, ans)
    
    return charCeil(arr, char, strt+1, end, ans)

charArr = ['a', 'f', 'j']
print(charCeil(charArr, 'z', 0, len(charArr)-1, ''))