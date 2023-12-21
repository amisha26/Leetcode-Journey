"""
Author: amisha26
Question Link: https://leetcode.com/problems/next-greater-element-i/
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        stack.append(10**32)
        i = 0
        d = {}
        while i < len(nums2):
            if nums2[i] > stack[-1]:
                x = stack.pop()
                d[x] = nums2[i]
            else:
                stack.append(nums2[i])
                i += 1
        ans = []
        for i in nums1:
            if i in d:
                ans.append(d[i])
            else:
                ans.append(-1)
        return ans