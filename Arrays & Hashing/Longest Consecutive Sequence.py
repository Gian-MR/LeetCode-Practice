"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest = 1
        current = 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            elif nums[i] + 1 == nums[i + 1]:
                current += 1
            else:
                longest = max(longest, current)
                current = 1

        return max(longest, current)
"""
"""
The plan of this was to sort the array first and then iterate through it to find the longest consecutive sequence. We keep track of the current sequence length and the longest sequence length found so far. If we encounter a number that is one more than the previous number, we increment the current sequence length. Otherwise, we update the longest sequence length if necessary and reset the current sequence length. Finally, we return the maximum of the longest and current sequence lengths.
"""