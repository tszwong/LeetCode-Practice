# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []: return None  # base case

        # setting the root node of the BST
        mid_val = len(nums) // 2
        root = TreeNode(nums[mid_val])

        # build left and right sides of the root node using recursion
        root.left = self.sortedArrayToBST(nums[:mid_val])
        root.right = self.sortedArrayToBST(nums[mid_val + 1:])

        # tree is completed when we get to this point so return the results
        return root


    # Time Complexity: O(n), we have to touch every element in the array
    # Space Complexity: O(n), we have to build a tree with n elements
