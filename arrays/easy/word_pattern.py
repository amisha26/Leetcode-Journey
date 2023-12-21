"""
Author: amisha26
Question Link: https://leetcode.com/problems/word-pattern/
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        d = {}
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if s[i] not in d.values():
                    d[pattern[i]] = s[i]
                else:
                    return False
            else:
                if d[pattern[i]] != s[i]:
                    return False
        return True 