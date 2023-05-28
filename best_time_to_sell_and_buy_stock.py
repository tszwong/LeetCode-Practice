class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        profit = 0
        min_p = prices[0] # initialize the min to first item of list

        # iterate through the prices
        for i in range(1, len(prices)):
            if prices[i] > min_p:
                # calculate profit
                profit = max(profit, prices[i]-min_p)
            else:
                min_p = prices[i] # update with new min

        return profit
