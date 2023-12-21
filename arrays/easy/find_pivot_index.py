"""
Author: amisha26
Question Link: https://leetcode.com/problems/find-pivot-index/
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s1 = [0]
        j = 0
        for i in range(len(nums)- 1, -1, -1):
            x = nums[i] + s1[j]
            j += 1
            s1.append(x)
        s2 = 0
        q = len(s1) - 1
        for i in range(len(nums)):
            if s1[q - 1] == s2:
                return i
            else:
                s2 += nums[i]
                q -= 1

        return -1