class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # keep count
        for i in range(len(nums)): # update entries, O(n)
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1

        # sort the items in dictionary
        sort = sorted(count.items(), key=lambda x: x[1]) # sort by the values, O(nlogn)
        sorted_d = [item[0] for item in sort] # add them to a list

        # add the k most frequet elements to the output list
        res = []

        # taking from the back of the list since it was sorted from least to most frequent
        k_in = len(res)-1
        for i in range(k): # O(k)
            res.append(sorted_d[k_in])
            k_in -= 1

        return res # overall time complexity -> O(n + mlogm + k)
        
