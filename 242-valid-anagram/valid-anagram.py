class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count=0
        if len(s) != len(t):
            return False
        l=list(t)
        for i in s:
            if i in l:
                count+=1
                l.remove(i)
        if count == len(s):
            return True
        else:
            return False