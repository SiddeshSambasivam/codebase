# Problem: https://leetcode.com/problems/maximum-product-subarray/
# Trick: Kadane's Algorithm for multiplication
# 1. Need to keep track of the minimum and maximum product as when a negative number comes up, it just inverts the maximum product
# 2. find the max and min product at each and every index and compare all three possibilities
#           (i)   max_i * nums[i]
#           (ii)  min_i * nums[i]
#           (iii) nums[i]
#    for finding the maz_i, min_i and the global maximum product


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Base cases
        if len(nums) == 0:
            return -1  # no element in the array

        if len(nums) == 1:
            return nums[0]  # return the array with only one element

        # at each position we need to know what is the maximum product value and the minimum product value

        prev_min = prev_max = max_product = nums[0]

        for i in range(1, len(nums)):

            # Two cases:
            # case 1: current element is positive then we need to compare with nums[i] and the product of the prev_max and the current ele
            # case 2: current element is negative then we need to compare with nums[i] and the product of the prev_min and the current ele

            current_max = max(prev_max*nums[i], prev_min*nums[i], nums[i])
            current_min = min(prev_max*nums[i], prev_min*nums[i], nums[i])

            prev_max, prev_min = current_max, current_min

            max_product = max(max_product, current_max)

        return max_product
