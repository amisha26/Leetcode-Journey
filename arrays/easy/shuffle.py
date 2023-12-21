"""
Author: amisha26
Question Link: https://leetcode.com/problems/shuffle-the-array/
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
        # Calculate the index of the second half element
            j = i + n
        # Rearrange elements in-place by swapping
            nums[i*2+1], nums[j] = nums[j], nums[i*2+1]
    
        return nums