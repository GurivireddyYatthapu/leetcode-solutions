class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        remain=[]
        count=0
        for i in nums:
            if i == 0:
                count +=1
            else:
                remain.append(i)
        remain.extend([0] * count)
        nums[:] = remain           
      