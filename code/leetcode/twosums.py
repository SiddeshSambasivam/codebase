# Problem: https://leetcode.com/problems/two-sum/
# Trick: use hashmap to check for compliments

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # only one solution exist
        compliments = {}

        for i, ele in enumerate(nums):

            compliment = target - ele
            if compliment in compliments.keys():
                return [compliments[compliment], i]

            compliments[ele] = i
