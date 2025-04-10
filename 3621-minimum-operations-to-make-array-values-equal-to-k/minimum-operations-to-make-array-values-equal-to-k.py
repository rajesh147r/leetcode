class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result=0
        s=set(nums)
        # if min(nums) > k:
        #     result=len(s)
        if min(nums) >= k :
            if k in s : s.remove(k)
            result=len(s)
        else:
            return -1
        return result