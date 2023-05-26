# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # first translate the nodes into a string representation
        num_l1 = ""
        num_l2 = ""
        
        while l1 != None:
            num_l1 += str(l1.val)
            l1 = l1.next
        while l2 != None:
            num_l2 += str(l2.val)
            l2 = l2.next

        # reverse using slice
        num_l1 = int(num_l1[::-1])
        num_l2 = int(num_l2[::-1])
        sum_num = str(num_l1 + num_l2)[::-1]

        # create a new linked list l3
        l3 = ListNode(0)
        curr = l3
        for i in sum_num:
            curr.next = ListNode(int(i))
            curr = curr.next
        return l3.next
