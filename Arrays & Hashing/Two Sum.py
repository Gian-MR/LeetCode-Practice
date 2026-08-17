class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i,j]

"""
El plan de este fue un simple nested loop q busca la suma de 2 numeros y devuelve q index fue el q nos dio el resultado

Imp: recordar como index con range
"""
