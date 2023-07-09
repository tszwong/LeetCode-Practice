# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # set some temporary pointers
        temp1 = list1
        temp2 = list2

        # create an output list
        res = ListNode(0)
        curr = res

        while temp1 and temp2: # run until either is at last node
            # compare the value of the nodes and update pointes
            if temp1.val >= temp2.val:
                curr.next = temp2
                temp2 = temp2.next
            else:
                curr.next = temp1
                temp1 = temp1.next
            
            curr = curr.next # set the curr node to the new node we added

        # in the case that one list had more nodes than the other
        # we will just add the rest of the nodes to the result list
        if temp1 == None:
            curr.next = temp2
        else:
            curr.next = temp1

        return res.next


        # Time Complexity: O(m + n) where m and n represent number of nodes in list1 and list2
        # Space Complexity: O(1)
