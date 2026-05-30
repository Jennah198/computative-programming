class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
            # Copy last row
        dp = triangle[-1][:]

        # Start from second last row to the top
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # Min sum for current element = value + min of two children
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]