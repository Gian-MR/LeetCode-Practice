"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1 

        while l < r:
            calc = numbers[l] + numbers[r]
            if (calc == target):
                return l + 1, r + 1
            elif (calc < target):
                l += 1
            else:
                r -= 1
        return []      
"""

"""
The plan of this was to use two pointers, one at the beginning and one at the end of the array. We calculate the sum of the elements at these two pointers. If the sum is equal to the target, we return the indices (1-indexed). If the sum is less than the target, we move the left pointer to the right. If the sum is greater than the target, we move the right pointer to the left. We continue this process until we find a pair that sums to the target or until the pointers meet.
"""