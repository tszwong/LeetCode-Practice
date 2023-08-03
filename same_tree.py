# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # helper function to traverse the binary trees
        def preorder(node, result):
            if not node:
                result.append(None)
                return

            result.append(node.val)
            preorder(node.left, result)
            preorder(node.right, result)


        # store the results of the traversal into two lists
        res_p = []
        res_q = []
        preorder(p, res_p)
        preorder(q, res_q)

        return res_p == res_q  # check if the preorder traversals of the two are equal

    
    # Time Complexity: O(n), we visit every node of the two trees in the preorder traversal
    # Space Complexity: O(n), we created two lists to store the traversal results
