class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        my_dict = {0:1}
        prefix_sum = 0
        res = 0
        for i in range(len(nums)):
            
            prefix_sum += nums[i]
            
            if prefix_sum - k in my_dict:
                res += my_dict[prefix_sum - k]
                
            if prefix_sum in my_dict:
                my_dict[prefix_sum] += 1
            else:
                my_dict[prefix_sum] = 1
        
                
        return res
                
            
        