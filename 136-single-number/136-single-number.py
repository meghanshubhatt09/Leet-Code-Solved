class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        result = nums[0]
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 0:
            return -1
        
        
        for i in range(1,len(nums)-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                result = nums[i]
                
        if nums[i+1] != nums[i]:
            result = nums[i+1]
        return result
            