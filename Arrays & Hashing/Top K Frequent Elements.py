"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        #fills the map
        for n in nums:
            count[n] = count.get(n, 0) + 1
            
        heap = []
        for n in count.keys():
            heapq.heappush(heap,(count[n], n)) #freq, number
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
"""

"""
The plan of this was to use a map to count the frequency of each number in the list. Then we used a heap to keep track of the top k frequent elements. We pushed the frequency and the number into the heap, and if the size of the heap exceeded k, we popped the smallest element. Finally, we extracted the numbers from the heap to get the result.
"""