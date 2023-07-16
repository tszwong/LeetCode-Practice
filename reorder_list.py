# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head: return # if given an empty linked list

        que = deque()
        node = head

        while True:  # add all of the nodes into the queue
            node = node.next
            if not node: break  # if None
            que.append(node)

        while que: # run until the queue is empty
            if head:
                temp = que.pop() # get the last element of queue
                head.next = temp # update next pointer
                head = head.next # update current pointer

            if head and len(que) > 0:
                temp = que.popleft() # get the first element of queue
                head.next = temp
                head = head.next
        
        head.next = None # point the last item of the linked list to None

    
    # Time Complexity: O(n), traverse the linked list of n items
    # Space Complexity: O(n), creation of the queue
