import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        n = len(nums)-k
        
        heapq.heapify(nums)
        
        for i in range(n+1):
            x = heapq.heappop(nums)
            
        return x
        