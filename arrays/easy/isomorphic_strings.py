"""
Author: amisha26
Question Link: https://leetcode.com/problems/isomorphic-strings/
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] not in d: 
                if t[i] not in d.values():
                    d[s[i]] = t[i]
                else:
                    return False
            else:
                if d[s[i]] != t[i]:
                    return False
        return True
                
        print(d) 
        return True