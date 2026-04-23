class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #store the length of the input list
        n = len(nums)           # n=4
        output = [1] * n        # output =[1,1,1,1]

        # left of i
        prefix = 1              #i = 0,1,2,3
        for i in range(n):
            output[i] = prefix      #store current prefix product.         output[0] = prefix = 1
            prefix *= nums[i]    #update prefix foe the newxt position.    prefix = prefix * nums[0] 

        # right of i 
        suffix = 1
        for i in range(n-1,-1,-1):
            output[i] *= suffix
            suffix *= nums[i]

        return output

