"""
Author: amisha26
Question Link: https://leetcode.com/problems/can-place-flowers/
"""

class Solution:
    def canPlaceFlowers(self, nums: List[int], n: int) -> bool:
        if n == 0:
            return True
        nums = [0] + nums + [0]
        i = 1
        while i < len(nums) - 1:
            if nums[i] == 0:
                if nums[i-1] == 0 and nums[i+1] == 0:
                    if n > 0:
                        nums[i] = 1
                        n = n - 1
                    if n == 0:
                        return True
            i += 1
        return False