class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l = []
        for i in arr:
            if arr.count(i) == i:
                l.append(i)
            else:
                l.append(-1)
        return max(l)