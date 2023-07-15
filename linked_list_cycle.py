# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        track = set() # used to keep track of the nodes
        temp = head # temporary pointer

        while temp:
            if temp in track: 
                return True # duplicate i.e. we've already seen the node
            
            track.add(temp) # update tracker
            temp = temp.next # update pointer

        return False

  # Time Complexity: O(n), we traverse through the entire linked list once
  # Space Complexity: O(n), we created a set that holds n nodes from linked list
