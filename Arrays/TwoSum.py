#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, value in enumerate(nums):
            if target-value in dic:
                return dic[target-value], index
            else:
                dic[value] = index
        return -1
