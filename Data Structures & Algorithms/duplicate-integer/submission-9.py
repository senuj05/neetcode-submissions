'''
understand:
Theres a array of nums, and if the same number in the list appeaars 
twice; we will have to return true. if not return false

Plan:
first we cal look for the edge cases
- if there is no valuse in the list, we return null

second : sort the list, this will put the any duplicates next to 
        each other

third : do a for loop and check wheather rhe previus number is 
        the same number as the current
        if it is the same number , we will return true
        otherwise we will return false

'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # check if thers values in the list
        if not nums:
            return False
        
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False