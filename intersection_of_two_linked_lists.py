# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # Approach 1, Set, uses O(m+n) space
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes_a = set()  # keep track of all the nodes we have seen

        # use temporary pointers to maintain originl linked lists structures
        tempA, tempB = headA, headB

        while tempA:  # add the nodes of list a into a set to track intersection
            nodes_a.add(tempA)
            tempA = tempA.next

        while tempB:  # traverse list b to find intersection
            if tempB in nodes_a:  # intersection found
                return tempB
            tempB = tempB.next

        return None  # no intersection

    
    # Time Complexity: O(n+m), traverse each linked list once
    # Space Complexity: O(n), created a set that holds n elements


    # Approach 2, Two Pointers, O(1) space
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA, tempB = headA, headB

        while tempA != tempB:
            if tempA: tempA = tempA.next
            else: tempA = headB

            if tempB: tempB = tempB.next
            else: tempB = headA
        
        return tempA

    # Time Complexity: O(n+m), traverse each linked list once
    # Space Complexity: O(1)
