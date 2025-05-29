class Solution:
    def convert(self, s: str, numRows: int) -> str:
         if numRows >= len(s) or numRows==1 : return s
         index, next=0, 1
         rows = [[] for _ in range(numRows)]
         for char in s:
            rows[index].append(char)
            if index == 0:
                next = 1
            elif index == numRows-1:
                next = -1
            index += next
         for i in range(numRows):
            rows[i]=''.join(rows[i])
         return ''.join(rows)