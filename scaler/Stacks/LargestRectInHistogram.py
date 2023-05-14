# Given 
# An array of integers A.
# A represents a histogram i.e A[i] denotes the height of the ith histogram's bar. Width of each bar is 1.

# FIND :  the area of the largest rectangle formed by the histogram.

# CONSTRAINTS
# 1 <= |A| <= 100000
# 1 <= A[i] <= 1000000000


# |           |
# |        |  |
# |        |  |
# |        |  |     |
# |  |     |  |  |  |
# |__|__|__|__|__|__|__
#    2  1  5  6  2   3  ( here, width of each bar is 1)


# APPROACH : 
# If we consider a bar with heigth x. Now, if we are able to find  heigth of bars
# which are either greater than or equal to x on both left and right side of x
# then, the area enclosed within these bars will have min common height of x
# and width will be (rigth bar ind - left bar ind) - 1

from collections import deque;

def largestRectangleArea(A):
        
    len_A = len(A)
    stack = deque()
    mod = 10**9 + 7
    
    # nearest small left
    # TC O(N), SC O(N)
    nsl = [-1]*len_A
    stack.append(0)

    for i in range(1, len_A):
        while(stack != deque([]) and A[stack[-1]] >= A[i]):
            stack.pop()

        if(stack != deque([])):
            nsl[i] = stack[-1]
            
        stack.append(i)

    # nearest small right
    nsr = [len_A]*len_A
    stack.clear()
    stack.append(len_A-1)
    nsr[-1] = len_A
    i = len_A-2
    while(i >= 0):
        while(stack != deque([]) and A[stack[-1]] >= A[i]):
            stack.pop()

        if(stack != deque([])):
            nsr[i] = stack[-1]
            
        stack.append(i)
        i -= 1
    
    # finding max area of rect from histogram
    ans = 0
    for i in range(len_A):
        area = (A[i] * (nsr[i]-nsl[i]-1))
        ans = max(ans, area)
        
    return ans%mod

print(largestRectangleArea([2,1,5,6,2,4,3,7,8]))