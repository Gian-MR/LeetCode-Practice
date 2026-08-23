"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l,r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0

        while(l < r):
            if maxL < maxR:
                l +=1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -=1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        
        return res
"""

"""
The plan of this was to use two pointers, one at the beginning and one at the end of the array. We keep track of the maximum height seen so far from both sides. At each step, we move the pointer with the smaller height towards the other pointer and update the maximum height seen so far from that side. We add the difference between the maximum height and the current height to the result.
"""
           

