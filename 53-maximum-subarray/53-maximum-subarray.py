class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = nums[0]
        final_result = nums[0]
        if len(nums) == 1:
            return res
        
        
        for i in range(1,len(nums)):
            
            res = max(nums[i],res+nums[i])
            
            final_result = max(final_result,res)
        
            
        return final_result
        