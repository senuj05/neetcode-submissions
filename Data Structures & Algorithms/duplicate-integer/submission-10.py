"""
UNDERSTAND:
There is an array given as nums and we will have to return true
if the same numbers occures more than once.
If not we will return false

PLAN:
Edge cases: check if there is anything on the array
Then sort the array
then use a for loop and check if the index i and i-1 are the same
values, if so, return TRUE otherwise FALSE
"""

# Implementation:

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # first we can check if there is anything on the list
        if not nums:
            return False

        # now we can sort the list
        nums.sort()
        # then we can check if the index and index+1 are teh same
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
        