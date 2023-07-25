class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_paths = math.comb(m+n-2, m-1)
        return num_paths
