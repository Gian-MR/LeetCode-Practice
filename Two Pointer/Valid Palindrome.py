"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
"""

"""
The plan of this was to create a new string that only contains alphanumeric characters and is in lowercase. Then, we check if this new string is equal to its reverse.
"""