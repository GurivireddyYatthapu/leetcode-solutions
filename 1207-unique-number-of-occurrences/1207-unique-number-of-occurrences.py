class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        frequency={}
        answer=[]
        for i in arr:
            frequency[i] = frequency.get(i,0) + 1
        for key,value in frequency.items():
            answer.append(value)
        return len(answer)==len(set(answer))        