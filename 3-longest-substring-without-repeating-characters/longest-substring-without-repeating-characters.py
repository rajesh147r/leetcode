class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i,len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                else: 
                    break
            max_len = max(max_len, len(seen))
        return max_len