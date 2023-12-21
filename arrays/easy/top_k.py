"""
Author: amisha26
Question Link: https://leetcode.com/problems/top-k-frequent-elements/description/
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        ans = []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
        for i in d:
            if k != 0:
                ans.append(i)
                k = k - 1   

        return ans