"""
Author: amisha26
Question Link: https://leetcode.com/problems/determine-if-two-strings-are-close/description/
"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        d1, d2 = {}, {}
        for i in word1:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1

        for i in word2:
            if i not in d2:
                d2[i] = 1
            else:
                d2[i] += 1

        if sorted(d1.values()) != sorted(d2.values()):
            return False
        else:
            return True