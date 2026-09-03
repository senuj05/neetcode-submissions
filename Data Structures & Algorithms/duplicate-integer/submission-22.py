class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #  edge case
        if not nums:
            return False

        # sort the array
        nums.sort()

        for i in range (len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False