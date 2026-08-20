"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums) -1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
        
"""
"""
The plan of this was to use two passes through the array. In the first pass, we calculate the prefix products and store them in the result array. In the second pass, we calculate the postfix products and multiply them with the existing values in the result array.
"""
