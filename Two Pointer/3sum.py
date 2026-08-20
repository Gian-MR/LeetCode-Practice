"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while(l < r):
                calc = a + nums[l] + nums[r]
                if calc > 0:
                    r -= 1
                elif calc < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]]) 
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res

"""

"""
The plan of this was to sort the array first and then iterate through it to find all unique triplets that sum to zero. For each element, we use two pointers to find pairs that sum with the current element to zero. We skip duplicates to ensure unique triplets.
"""