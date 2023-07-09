# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # in case we need to remove the head of the list
        temp = ListNode(0)
        temp.next = head
        # use fast and slow pointers
        fast = temp
        slow = temp
        
        for i in range(n): # move the fast pointer n steps ahead of slow
            fast = fast.next

        while fast.next: # move pointers until the fast pointer reaches end
            fast = fast.next
            slow = slow.next

        # by the time we are here the slow pointer is pointing at the nth node
        slow.next = slow.next.next
        
        return temp.next

  # Time Complexity: O(n)
  # Space Complexity: O(1)
