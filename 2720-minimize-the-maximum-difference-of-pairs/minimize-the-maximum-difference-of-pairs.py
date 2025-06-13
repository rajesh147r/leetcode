class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def can_form_pairs(max_diff):
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  # skip both indices since they are paired
                else:
                    i += 1
            return count >= p

        low = 0
        high = nums[-1] - nums[0]
        result = high

        while low <= high:
            mid = (low + high) // 2
            if can_form_pairs(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result
