from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        
        max_odd = 0
        min_even = len(s)
        for i in freq.values():
            if i%2 == 0:
                min_even = min(min_even, i)
            else:
                max_odd = max(max_odd, i)
        return max_odd-min_even