class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge both arrays into one list
        combined= nums1 + nums2
        # sort the list
        combined.sort()

        # get the tot length, if the tot length is odd, return mid ele
        #  if its even, return avg of the two mid element
        tot_len = len(combined)

        if tot_len % 2 == 0:
            return (combined[tot_len // 2-1]+ combined[tot_len//2]) /2.0
        else:
            return combined[tot_len//2]