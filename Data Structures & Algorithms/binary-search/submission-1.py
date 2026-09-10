class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #  crate two pointers
        left, right = 0, len(nums)-1

        # next we compate the mid index with the taget
        while left <= right:
            # middle index
            mid = (left + right )// 2
            if nums[mid] < target :
                left = mid +1
            elif nums[mid]> target :
                right = mid -1
            else:
                return mid
        return -1