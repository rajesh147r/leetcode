class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        count = n//m
        divisible = m*count*(count+1)
        total=n*(n+1)//2
        return total-divisible