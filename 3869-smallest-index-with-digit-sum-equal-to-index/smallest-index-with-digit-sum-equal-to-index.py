class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            current=0
            val=nums[i]
            while val:
                current+=val%10
                val=val//10
            if current==i:
                return i
        else:
            return -1