# FInd the floor value of a number from the given arr 

# Given : Number, arr 
# To find : floor value

# iterative method
A = [1,3,4,5,6,7,8,19,23,45,67,83,92]
# TC log(n) , SC O(1)
def floor(arr, num):
    
    len_arr = len(arr)
    strt = 0
    end = len_arr-1
    ans = 0
    while(strt <= end):
        mid = strt + (end-strt)//2
        
        if(arr[mid] <= num):
            ans = arr[mid]
            strt = mid+1
        else:
            end = mid-1
    
    return ans


# print(floor(A,12))

# recursive method 
# TC log(n) , SC log(n) 
def floorRecursive(arr, num, strt, end, floor):
    if(strt > end):
        return floor
    
    mid = strt + (end-strt)//2

    if(arr[mid] <= num):
        return floorRecursive(arr, num, mid+1, end, arr[mid])
    else:
        return floorRecursive(arr, num, strt, mid-1, floor)

print(floorRecursive(A, 19, 0, len(A)-1, -1))