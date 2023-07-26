# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Approach 1, DFS recursively, faster than DFS iteratively but more space used
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        if not root: return 0  # base case

        # recursive case
        left_side = self.maxDepth(root.left)
        right_side = self.maxDepth(root.right)

        return 1 + max(left_side, right_side)



    # Approach 2, DFS iteratively (preorder traversal with stack), slower that DFS recursively but less space used
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root: return 0  # base case

        stack = [[root, 1]]  # [ [root], [depth] ]
        res = 1

        while stack:  # run until stack is empty i.e. at the end of the tree
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])

        return res



    # Approach 3, BFS, overall best solution in terms of time and space
    def maxDepth3(self, root: Optional[TreeNode]) -> int:
        if not root: return 0  # base case

        level = 0  # track the depth
        q = deque([root])  # initialize a queue with the root

        while q:  # run until queue is empty i.e. at the end of the tree
            for i in range(len(q)):
                node = q.popleft()  # FIFO

                # add the children to the queue if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1  # update depth counter

        return level
