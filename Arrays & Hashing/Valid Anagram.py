class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_s = {}
        for letra in s:
            map_s[letra] = map_s.get(letra, 0) + 1

        map_t = {}
        for letra in t:
            map_t[letra] = map_t.get(letra, 0) + 1

        return map_s == map_t

    """
    Plan de este fue usar un map para poder contar cuantas veces salia una letra en la palabra. Hicimos esto para los dos strings s y t. Luego de hacer los dos mapas comparamos si los dos mapas son iguales. Si los mapas son iguales ps es un anagram y sino ps no es un anagram
    """
