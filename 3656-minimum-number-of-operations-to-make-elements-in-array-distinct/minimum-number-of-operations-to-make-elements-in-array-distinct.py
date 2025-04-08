# class Solution:
#     def minimumOperations(self, nums: List[int]) -> int:
#         s=set(nums)
#         result=1
#         if len(nums) != len(s):
#             nums=nums[3:]
#             result += 1
#         else:
#             return 0
#         return result
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        while len(nums) != len(set(nums)):
            nums = nums[3:]  # remove first 3 elements
            operations += 1
        return operations
