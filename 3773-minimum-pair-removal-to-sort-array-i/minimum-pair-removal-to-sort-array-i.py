class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations=0
        def is_descending(arr):
            return all(arr[i]<=arr[i+1] for i in range(len(arr)-1))
        while not is_descending(nums):
            value=float('inf')
            for i in range(len(nums)-1):
                pair_sum=nums[i]+nums[i+1]
                if pair_sum < value:
                    value=pair_sum
                    index=i
            nums= nums[:index]+[value]+nums[index+2:]
            operations+=1
        return operations
