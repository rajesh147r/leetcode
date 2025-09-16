class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = 0
        res = []
        for c in s:
            if c=='(':
                if n>0:
                    res.append(c)
                n+=1
            else:
                if n > 1:
                    res.append(c)
                n -= 1
        return "".join(res)