from collections import defaultdict


class Solution: # type: ignore
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

#sorting        
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

#hasmap
class Solution:  # noqa: F811
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        res = defaultdict(list) #this is to evade an edgecase
        for s in strs:
            count = [0] * 26 #a-z
            
            for c in s:
                count[ord(c) - ord("a")] += 1 #this takes the asci number and substracts it with "a" for it to be ex: a - a = 0 -> b - a = 1
            res[tuple(count)].append(s) #the tuple is bc of python

        return list(res.values())
