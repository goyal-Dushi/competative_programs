class TreeNode:
    def __init__(self, value):
         self.val = value
         self.left = None
         self.right = None

def solve(self, A):

    len_A = len(A)
    if(len_A == 1):
        head = TreeNode(A[0])
        return head

    head = TreeNode(A[0])
    node_arr = [head]
    i=0
    left_ind = i
    right_ind = i
    while(i < len_A):
    # if curr node is none, then , there won't be any of its children
        if(node_arr[i] == None):
            i += 1
            continue

        # left child ind in arr
        left_ind = right_ind + 1
        # right child ind in arr
        right_ind = left_ind + 1
        if(left_ind >= len_A or right_ind >= len_A):
            break
        
        # get access to current node from arr
        temp_node = node_arr[i]
        
        # assign its left child
        if(A[left_ind] != -1):
            temp_node.left = TreeNode(A[left_ind])
            node_arr.append(temp_node.left)
        else:
            node_arr.append(None)

        # assign right child
        if(A[right_ind] != -1):
            temp_node.right = TreeNode(A[right_ind])
            node_arr.append(temp_node.right)
        else:
            node_arr.append(None)

        i += 1
        
    return head