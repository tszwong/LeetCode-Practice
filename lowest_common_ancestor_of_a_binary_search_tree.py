# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # Approach 1: iterative
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:  # traverse the binary tree
            if p.val < root.val and q.val < root.val:  # current node is greater than both p and q nodes
                root = root.left  # go to the left subtree
            elif p.val > root.val and q.val > root.val:  # current node is less than both p and q nodes
                root = root.right
            else:  # one of p or q is less than current node and the other is greater than current node
                # we have found the lowest common ancestor since p and q are its children
                return root

    
    # Time Complexity: O(n), where n is the height of the bst, O(logn) best case
    # Space Complexity: O(1), variables used for traversal



    # Approach 2: recursive
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
            if p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            elif p.val > root.val and q.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q)
            else: 
                return root


    # Time Complexity: O(n), where n is the height of the bst, O(logn) best case
    # Space Complexity: O(n), worst case we have to do n recursive calls i.e. completely unbalanced tree
