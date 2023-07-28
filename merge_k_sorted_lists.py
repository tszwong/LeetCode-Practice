# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None  # edge case

        while len(lists) > 1: 
            merged = []  # what has been merged so far

            for i in range(0, len(lists), 2):  # merge two lists at a time, O(logk)
                list1 = lists[i] 

                if i + 1 < len(lists):  # check if there's another list to merge with
                    list2 = lists[i + 1]
                else: list2 = None

                # add the merged results of l1 and l2 to the merged results
                merged.append(self.merge(list1, list2))

            lists = merged[:]  # update original list for the iteration

        # since there will be one merged final list in the end,
        # we can simply return the first and only item in lists
        return lists[0]


    # Time Complexity: O(nlogk) where n = nodes in linked lists and k = number of lists, 
    # we are merging two lists each iteration and we visit each node of the lists
    
    # Space Complexity: O(k), the complexity is O(k/2 + k/4 + k/8 + ... + 1) = O(k) during the merging process



    # helper function that merges two given lists
    def merge(self, list1, list2):
        # Use a dummy node to simplify the code
        dummy = ListNode(0)  # keeps a reference to the front of the list
        curr = dummy

        while list1 and list2:  # run until at the end of either list
            if list1.val <= list2.val:  # find smaller value and update pointers accordingly
                curr.next = list1
                list1 = list1.next  # since these lists are local to merge() we don't need to maintain the structure of the lists
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next  # update pointer

        # Add the remaining nodes from list1 or list2
        curr.next = list1 or list2

        # Return the merged list starting from the node after the dummy node
        return dummy.next
