"""
Author: amisha26
Question Link: https://leetcode.com/problems/longest-common-prefix/description/
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            x = strs[i]
            s = ""
            if x == "" or prefix == "":
                return ""

            min_len = min(len(prefix), len(x))

            for j in range(min_len):
                if x[j] == prefix[j]:
                    s += x[j]
                else:
                    break
            prefix = s

        return prefix