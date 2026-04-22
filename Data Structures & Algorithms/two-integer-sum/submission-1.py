class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # here we are using brute force
        for i in range(len(nums)):               #outer loop : picks the first number
            for j in range (i+1, len(nums)):    # inner : picks the second number , i starts at index 0 and i+1 starts one ahaed
                if nums[i] + nums[j] == target: # check whether the two numbers equal to the
                    return [i,j] # if find a valid pair, return their indices

        