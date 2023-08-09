# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None  # edge case, empty tree

        stack = []  # use a stack to store nodes visited
        dummy = root  # use a dummy node to traverse tree

        # helper function for dfs
        def dfs(root):  
            if root:  # inorder = l, root, r
                dfs(root.left)
                stack.append(root.val)
                dfs(root.right)

        
        dfs(dummy)  # call the helper function

        return stack

    
    # Time Complexity: O(n). we visit every node of the binary tree
    # Space Complexity: O(n), we store all n nodes of the binary tree in the stack
