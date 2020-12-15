# Problem: https://leetcode.com/problems/contains-duplicate/
# Methods
# Method 1: Use a hash table for faster look up O(1) -> O(n)
# Method 2: Sort the list and check if consecutive elements are equal -> O(n) + O(nlogn)
# Method 3: Use set() to make all the elements unique and compare len with the original list
# len() takes O(1)
# converting from list to set takes  O(n)

'''
A == B       # A is equivalent to B

A != B       # A is not equivalent to B

A <= B    # A is subset of B A <B>= B    

A > B     # A is proper superset of B

A | B        # the union of A and B

A & B     # the intersection of A and B

A - B        # the set of elements in A but not B

A ˆ B        # the symmetric difference

a = {x for x in A if x not in 'abc'}   # Set Comprehension
'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # use to set to get unique
        # converting list to set takes O(n)
        # len() cost O(1) as its a constant look up independent of the size of the list

        if len(set(nums)) == len(nums):
            return False
        else:
            return True
