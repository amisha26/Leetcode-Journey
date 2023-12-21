"""
Author: amisha26
Question Link: https://leetcode.com/problems/range-sum-query-immutable/
"""

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pre = [self.nums[0]]
        for i in range(1, len(self.nums)):
            x = self.nums[i] + self.pre[i - 1]
            self.pre.append(x)
        print(self.pre)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.pre[right] - 0
        else:
            return self.pre[right] - self.pre[left - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)