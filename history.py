
# Qestion 1: Two Sum
# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index,value in enumerate(nums):
            if target - value in d:
                return [index,d[target-value]]

            d[value]=index