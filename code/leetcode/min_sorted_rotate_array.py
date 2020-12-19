import math

# Problem:
# Trick:
# 1. Binary Search algorithm can be modified to any specific sorted array related problem
# 2. Also BS gives the optimal solution of O(logn)


class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Base Case 1: Array with only one element
        if len(nums) == 1:
            return nums[0]

        # Base Case 2: Array already sorted
        if nums[len(nums)-1] > nums[0]:
            return nums[0]

        l, r = 0, len(nums)-1

        while r > l:

            mid = math.floor((l+r)/2)

            if nums[mid] > nums[mid+1]:
                return nums[mid+1]

            if nums[mid] < nums[mid-1]:
                return nums[mid]

            if nums[mid] > nums[0]:

                l = mid+1

            else:

                r = mid
