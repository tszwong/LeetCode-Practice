class Solution:
    def maxArea(self, height: List[int]) -> int:
      
        # first approach, brute force approach, nested for loop O(n^2)
        # will exceed memory limit when given a big list of heights
        # 
        # areas = []
        # for i in range(len(height)):
        #     for j in range(1, len(height)):
        #         h = min(height[i], height[j]) # calculate the height
        #         w = j-i # calculate the width
        #         areas.append(h*w)
        # return max(areas)

        # second approach, the much better approach O(n)
        # using two pointers
        area = 0 
        left = 0
        right = len(height)-1

        while left < right:
            # calculate the area
            curr_area = (right - left) * min(height[left], height[right])
            area = max(area, curr_area)

            # update the pointers, move the one with the smaller value
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area
