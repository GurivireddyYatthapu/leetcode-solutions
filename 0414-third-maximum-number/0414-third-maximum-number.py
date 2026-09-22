class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        n=len(nums)
        first=float('-inf')
        second=float('-inf')
        third=float('-inf')
        for i in nums:
            if i in (first,second,third):
                continue
                
            if i > first:
                third=second
                second=first
                first=i
            elif  i > second:
                third=second
                second=i
            elif i > third:
                third=i
            
        return third if third !=float('-inf') else first

        