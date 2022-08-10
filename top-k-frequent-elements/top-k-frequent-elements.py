
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_dict = {}
        for i in range(len(nums)):
            freq_dict[nums[i]] = freq_dict.get(nums[i], 0) + 1
            
        my_list = [(-value,key) for key, value in freq_dict.items()]
            
            
        heapq.heapify(my_list)
        res = []
        for i in range(k):
            res.append(heapq.heappop(my_list)[1])
        return res
            
        
        