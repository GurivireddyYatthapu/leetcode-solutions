class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.sort()
        small = nums[:(n+1)//2]
        large = nums[(n+1)//2:]
        small.reverse()
        large.reverse()
        i = 0
        while i < len(small):
            nums[2 * i] = small[i]
            i += 1
        j = 0
        while j < len(large):
            nums[2 * j +1] = large[j]
            j += 1    