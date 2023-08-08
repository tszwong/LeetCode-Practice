# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Approach 1, has a better average case complexity and uses less space for best case
    def kthSmallest1(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return None  # edge case, given an empty binary tree

        stack = []  # use a stack to track the nodes we have seen during traversal
        dummy = root  # temp pointer node


        while True:  # perform inorder traversal
        
            while dummy:  # traverse to the leftmost node and push nodes to stack
                stack.append(dummy)
                dummy = dummy.left  # move to smallest child each time

            top = stack.pop()
            k -= 1  # update to track number of nodes visited
            if k == 0: return top.val  # if match with k return that node's value

            # move to the right subtree if we haven't reached the kth smallest node yet
            dummy = top.right

    # Time Complexity: O(n), worst case we will visit all n nodes
    # Space Complexity: O(n), worst case the stack will hold all n nodes



    # Approach 2, straight-forward, has a worse average case complexity
    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        stack = []  # List to store the inorder traversal
    
        def inorder(node):
            if node:
                inorder(node.left)  # Traverse the left subtree
                stack.append(node.val)  # Visit the current node
                inorder(node.right)  # Traverse the right subtree
                
        helper(root)
        return stack[k-1]

    # Time Complexity: O(n), we will visit all n nodes
    # Space Complexity: O(n), stack will hold all n nodes
