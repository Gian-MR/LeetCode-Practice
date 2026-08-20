"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0

        while(l < r):
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1
        
        return res
"""

"""
The plan of this was to use two pointers, one at the beginning and one at the end of the array. We calculate the area between these two pointers and keep track of the maximum area found so far. We move the pointer with the smaller height towards the other pointer to try to find a larger area. We continue this process until the pointers meet.
"""
        
