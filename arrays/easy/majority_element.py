"""
Author: amisha26
Question Link: https://leetcode.com/problems/majority-element/
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums) // 2
        d = {}
        m = -1
        e = 1
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                if d[i] > m:
                    m = d[i]
                    e = i
        return e