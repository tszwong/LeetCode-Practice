class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [] # array to hold results

        for interval in intervals:
            if newInterval[0] > interval[1]: # the new interval starts after current interval
                res.append(interval)

            elif newInterval[1] < interval[0]: # the new interval starts before current interval
                res.append(newInterval) # add the new interval into array
                newInterval = interval # set new interval to current interval

            else: # when the new interval is within other intervals
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        res.append(newInterval) # adding the extra interval
        return res


    # Time Complexity: O(n), traversing through the array with n intervals
    # Space Complexity: O(n), new array to hold the result
