class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        arr = [''] * numRows
        current, dir = 1, 1
        arr[0] += s[0]

        for char in s[1:]:
            arr[current] += char
            if current % (numRows - 1) == 0:
                dir = -dir
            current += dir

        return ''.join(arr)
