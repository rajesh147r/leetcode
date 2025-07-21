class Solution:
    def makeFancyString(self, s: str) -> str:
        result = s[0]
        c = 1
        for a in s[1:]:
            if a == result[-1]:
                c += 1
                if c < 3:
                    result += a
            else:
                c = 1
                result += a
        return result