class Solution:
    def minMaxDifference(self,num: int) -> int:
        s = str(num)
        max_val = num
        min_val = num
        for d in '0123456789':
            for r in '0123456789':
                if d == r:
                    continue
                new = int(s.replace(d, r))
                max_val = max(max_val, new)
                min_val = min(min_val, new)
        return max_val - min_val

            