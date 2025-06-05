class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        # if n == 3:
        #     if sum(nums) == 0:
        #         return [nums]
        #     else:
        #         return []
        nums.sort()
        result = []
        for i in range(n):
            if nums[i] == nums[i-1] and i > 0:
                continue
            j = i+1
            k = n-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k-=1
                elif total < 0:
                    j+=1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
                    while nums[k] == nums[k+1] and k > j:
                        k-=1
        return result
                