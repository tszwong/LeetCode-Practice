class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0: return []

        # let's sort the arrays based on the smaller values
        a = sorted(intervals, key=lambda x: x[0])
        res = [a[0]] # put the first item into our result list

        # two pointers
        l = 0
        r = 1
        while r <= len(intervals)-1: # run until right pointer hits end of list
            if res[l][1] >= a[r][0]: # overlap occurs
                res[l][1] = max(res[l][1], a[r][1]) # take the max of the two intervals' right values
            else: # no overlap
                res.append(a[r]) # add the current interval to res
                l += 1 # move the res pointer to added interval
            r += 1 # move the pointer for a to the right

        return res

        # Time Complexity: O(nlogn)
        # the sorting method takes ～O(nlog) and the iterating
        # is O(n) since we need to visit every interval so overall
        # time complexity is O(nlogn) since nlogn > n

        # Space Complexity: O(n) the array to hold the result intervals
