class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = {}
        for val, weight in items1 + items2:
            d[val] = d.get(val, 0) + weight
        return sorted([[val, weight] for val, weight in d.items()])