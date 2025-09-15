class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        ls1 = list(brokenLetters)
        for word in text.split():
            if not any(ch in ls1 for ch in word):
                count += 1
        return count