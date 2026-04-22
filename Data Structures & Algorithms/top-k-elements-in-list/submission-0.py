class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # step 1: count frequencies
        count ={}
        for n in nums:
            count[n] = count.get(n,0) +1
        
        # step 2: create buckets (index = frequancy)
        # max frequancy posible is len(nums)
        freq = [[]for _ in range(len(nums)+1)]

        # step 3: place numbers in their  freguancy bucket
        for num, cnt in count.items():
            freq[cnt].append(num)

        # step 4: collect top k from the higherst down
        res= []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res