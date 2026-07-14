class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums

    def add(self, val: int) -> int:
        # append val to the array
        self.arr.append(val)
        # sort the array
        self.arr.sort()
        # return the elemetn at index len(arr)-k*( the kth largest)
        return self.arr[len(self.arr)- self.k]
