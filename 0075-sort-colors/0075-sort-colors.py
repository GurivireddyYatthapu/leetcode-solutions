class Solution:
    def sortColors(self, arr: List[int]) -> None:
        n=len(arr)
        if n <=1:
            return arr
        for i in range(n):
            for j in range(0,n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr            