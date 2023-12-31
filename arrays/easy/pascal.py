"""
Author: amisha26
Question Link: https://leetcode.com/problems/pascals-triangle/
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        for i in range(1, numRows): # for n = 2
            l = [0] * (i + 1)  #  
            l[0], l[-1] = 1, 1
            x = res[-1]
            for j in range(1, len(l) - 1):
                l[j] = x[j - 1] + x[j]
            res.append(l)
        return res