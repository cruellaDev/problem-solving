# https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def twoSum(self, nums, target):
        answer = {}
        for i, x in enumerate(nums):
            if x in answer:
                return [answer[x], i]
            else:
                answer[target - x] = i

'''
class Solution(object):
    def twoSum(self, nums, target):
        for i, x in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if x + nums[j] == target:
                    return[i, j]
'''
        