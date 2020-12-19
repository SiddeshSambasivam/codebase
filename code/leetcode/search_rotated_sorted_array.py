# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Trick:
# 1. Using binary search to find the index of the first element, which is the number of rotations
# 2. do normal binary search, whenever calculating the mid, just add the rotations

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Primary Base Case
        if len(nums) == 1:

            # Secondary Base Case
            if nums[0] != target:
                return -1

            return 0

        return self.linear(nums, target)    # O(n)

        return self.binary_search(nums, target)  # O(logn)

    def binary_search(self, nums: List[int], target: int) -> int:

        start = 0
        if nums[0] > nums[len(nums)-1]:

            # array is rotated, we find the starting index
            r, l = len(nums)-1, 0
            while r > l:

                mid = math.floor((r+l)/2)

                if nums[mid] > nums[mid+1]:
                    start = mid+1
                    break

                if nums[mid] < nums[mid-1]:
                    start = mid
                    break

                if nums[mid] > nums[0]:
                    l = mid+1
                else:
                    r = mid

        r, l = len(nums)-1, 0

        while r >= l:

            mid = math.floor((r+l)/2)

            offset_mid = (mid+start) % len(nums)

            if nums[offset_mid] == target:

                return offset_mid

            if nums[offset_mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1

    def linear(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):

            if nums[i] == target:
                return i

        return -1
