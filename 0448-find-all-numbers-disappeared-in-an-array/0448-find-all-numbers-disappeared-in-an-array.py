class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for i in nums:
            a=abs(i) - 1
            nums[a]=-abs(nums[a])
        return [a+1 for a,i in enumerate(nums) if i > 0]    
        