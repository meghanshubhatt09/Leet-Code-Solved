class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = [0]*(max(nums)+1)
        
        for i in range(len(nums)):
            n[nums[i]] += 1
        for j in range(len(n)):
            if n[j]==0:
                return j
        return max(nums)+1
        