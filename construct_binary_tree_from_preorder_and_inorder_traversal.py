# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return None  # edge cases, if either list given is empty

        root = TreeNode(preorder[0])  # initiated root node of the tree
        mid = inorder.index(preorder[0])

        # build the left and right sides of the tree
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])  # the left side of the tree is the left of root in inorder
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])  # the right side of of tree is right of root in inorder

        return root  # return the root of the tree


    # Time Complexity: O(n^2), worst case index() would take O(n) to find element and we have to do it for every node 
    # Space Complexity: O(n), worst case would result in a binary tree with a height of n
