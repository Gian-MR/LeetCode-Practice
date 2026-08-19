class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: list[int]
        :rtype: bool
        """
        set_nums = set(nums)

        return len(nums) != len(set_nums)

    """
    El plan de este fue poner la lista en un set. Ya q el set quita las letras duplicadas. Luego ponemos len(nums) para poder sacar el tamaño de nums y lo comparamos al tamaño del set de nums. Si los tamaños son iguales sale false (no tiene duplicados), Si sale diferente sale true (tenia un duplicado)
    
    """