# Problem: https://leetcode.com/problems/maximum-subarray/
# Trick: DP Problem (Kadane's Algorithm)
# 1. remember the max value of sum at each index. More like a greedy approach

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Time complexity: O(n)
        # Space complexity: O(1)
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] = max(nums[i], nums[i-1]+nums[i])

        return max(nums)
