class Solution:
    def splitArray(self, nums: List[int]) -> int:
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5)+1):
                if num%i == 0:
                    return False
            return True
        a, b = 0, 0
        for i in range(len(nums)):
            if is_prime(i):
                a += nums[i]
            else:
                b += nums[i]
        return abs(a-b)