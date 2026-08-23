class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        res = set(nums[0])
        for arr in nums[1:]:
            res &= set(arr)
        return sorted(list(res))