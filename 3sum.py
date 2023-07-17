class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3: return []
        
        trips = set()
        neg = []
        pos = []
        zero = []

        # categorize all of the numbers
        for num in nums:
            if num == 0: zero.append(num)
            if num < 0: neg.append(num)
            else: pos.append(num)

        # this is for lookup when we traverse the arrays
        n = set(neg)
        p = set(pos)

        # triplets involving zeros
        if len(zero) > 0:

            if len(zero) >= 3:
                trips.add((0,0,0))

            for num in p:  # triplets with 1 zero
                if -num in n:  # check if complement exists
                    trips.add((-num, 0, num))

        # checking negative numbers and its complement
        for i in range(len(neg)):
            
            for j in range(i+1, len(neg)):
                curr = neg[i] + neg[j]
                comp = -curr  # complement

                if comp in p:
                    trips.add(tuple(sorted([neg[i],neg[j], comp]))) # we want to sort so we can check for duplicates

        # checking positive numbers and its complement
        for i in range(len(pos)):
            
            for j in range(i+1, len(pos)):
                curr = pos[i] + pos[j]
                comp = -curr  # complement

                if comp in n:
                    trips.add(tuple(sorted([pos[i],pos[j], comp]))) # we want to sort so we can check for duplicates

        return trips

    
    # Time Complexity: O(n^2), nested for loop
    # Space Complexity: O(n), sets and arrays
