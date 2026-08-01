class Solution:
    def predictTheWinner(self, arr: list[int]) -> bool:
        total = sum(arr)
        
        def dp(i, j):
            if i == j:
                return arr[i]
            if i > j:
                return 0
            
            left = arr[i] - dp(i + 1, j)
            right = arr[j] - dp(i, j - 1)
            
            return max(left, right)
        
        return dp(0, len(arr) - 1) >= 0