'''
alg:
1. initialize both pointers left and right to 0
2. copy the current element at right to position left
3. skip all duplicates by advancing r while consecutive elements are equal
4. move left forward to prepare for the next unique elemeny
5. return left as the count of unique element

edge cases: 
'''


class Solution:
    # define the class method
    # taked an array 'nums' and returns an integer
    def removeDuplicates(self, nums: List[int]) -> int:
        #edge cases : if the array is empty return 0
        if not nums:
            return o

        k=1 # track where the next unique element should be placed
            # we start at 1 bcs the first element (index=0)

        #loop through the array starting at index 1 (skip the first
        # element since its already in place)
        for i in range(1, len(nums)):
            #compare the current element with the previous
            if nums[i]!= nums[i-1]:
                #place the unique element at position k
                nums[k]=nums[i]
                # increment k so the nexr unique element goes to the next position
                k+=1
        return k



        