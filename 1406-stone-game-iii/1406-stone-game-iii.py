class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 3

        for i in range(n - 1, -1, -1):
            max_diff = float('-inf')
            take_sum = 0
            
            for k in range(1, 4):
                if i + k <= n:
                    take_sum += stoneValue[i + k - 1]
                    max_diff = max(max_diff, take_sum - dp[k - 1])
            
            dp = [max_diff] + dp[:2]

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"