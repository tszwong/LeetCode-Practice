# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # helper function to traverse the binary trees
        def traverse(root):
            if root:  # return the value of current node and its left and right subtrees
                # we need the # because e.g. '1 None None' is in '31 None None' so we 
                # need to separate it so it becomes '#1 None None' and '#31 None None'
                return f"#{root.val} {traverse(root.left)} {traverse(root.right)}"
            else: 
                return None  # node is empty i.e. child doesn't exist


        # call the helper function
        str_root = traverse(root)
        str_subroot = traverse(subRoot)


        # print statements to check the string representations of the two trees
        # print(str_root)
        # print(str_subroot)


        return str_subroot in str_root  # return whether string representation of subroot is in root


  # Time Complexity: O(n), checking if str_subroot is present in str_root takes O(m * n) so O(n + mn) but n will dominate in a large sample
  # Space Complexity: O(n), worst case scenario we have n call stacks for recursively traversing the trees
