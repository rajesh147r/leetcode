class Solution:
    def kthCharacter(self, k: int) -> str:
        result = 'a'
        while len(result) < k:
            temp = ''
            for i in result:
                temp += chr(ord(i)+1)
            result += temp
        return result[k-1]