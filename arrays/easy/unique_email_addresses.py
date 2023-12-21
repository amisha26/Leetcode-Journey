"""
Author: amisha26
Question Link: https://leetcode.com/problems/unique-email-addresses/
"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = {}
        for i in emails:
            x = i.split("@")
            s = ""
            for j in x[0]:
                if j != '.' and j != '+':
                    s += j
                elif j == '+':
                    break
            if s + '@' + x[1] not in d:
                d[s + '@' + x[1]] = 1
        return len(d)