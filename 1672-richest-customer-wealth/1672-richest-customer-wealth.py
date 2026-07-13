class Solution:
    def maximumWealth(self, nums: List[List[int]]) -> int:
        add=0
        for i in range(len(nums)):
            maxx=0
            for j in range(len(nums[0])):
                maxx=maxx+nums[i][j]
            if maxx>add:
                add=maxx    
        return add        