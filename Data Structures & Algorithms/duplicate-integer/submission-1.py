'''
here, we can use two pointers
first go with the edge cases ; check weather the nums list is empty or not
then, check if the previous item is the same as the present item
if so, move the unique element to the position k
increment k for the next unique element
then return the number of unique elements 
'''


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
           return False
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False