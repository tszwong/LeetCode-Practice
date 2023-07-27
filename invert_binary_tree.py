# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None  # base case

        # swapping before the recursive calls strategy utilizes a preorder traversal
        # swapping after the recursive calls strategy utilizes a postorder traversal

        temp = root.left # use a temporary variable to store one side of the tree
        root.left = root.right # swap left with right
        root.right = temp # swap right with left stored in temp

        # recursion
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    
    # Time Complexity: O(n), we go through every node of the tree
    # Space Complexity: O(n) if tree is skewed, O(logn) if tree is balanced
