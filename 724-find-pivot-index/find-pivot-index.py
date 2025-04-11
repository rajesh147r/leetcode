class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum=0
        total=sum(nums)
        for i in range(len(nums)):
            r_sum=total-l_sum-nums[i]
            if r_sum == l_sum:
                return i
            l_sum+=nums[i]
        return -1