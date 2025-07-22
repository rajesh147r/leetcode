class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        init_sum = 0
        max_sum = 0
        i = 0
        seen = set()
        for j in range(len(nums)):
            while nums[j] in seen:
                seen.remove(nums[i])
                init_sum -= nums[i]
                i += 1
            seen.add(nums[j])
            init_sum += nums[j]
            max_sum = max(init_sum, max_sum)
        return max_sum