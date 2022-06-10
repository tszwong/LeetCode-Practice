class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        wealth = [sum(i) for i in accounts]
        max_wealth = max(wealth)
        
        return max_wealth
        
