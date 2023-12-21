"""
Author: amisha26
Question Link: https://leetcode.com/problems/valid-anagram/
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=list(s)
        b=list(t)
        a.sort()
        b.sort()
        if a==b:
            return True
        else:
            return False