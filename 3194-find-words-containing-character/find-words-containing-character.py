class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for ind, word in enumerate(words):
            if x in word:
                result.append(ind)
        return result