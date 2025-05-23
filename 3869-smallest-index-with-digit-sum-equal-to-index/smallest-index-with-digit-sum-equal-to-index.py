class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s=sum(int(x) for x in str(nums[i]))
            if s==i:
                return i
        else:
            return -1