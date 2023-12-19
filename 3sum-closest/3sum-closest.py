class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        result = prev_difference = 10000
        
        
        
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i+1
            end = len(nums) - 1
            
            while(start < end):
                
                if (sumx := nums[i] + nums[start] + nums[end]) == target:
                    return sumx
                
                
                difference = abs(target - sumx)
                if difference < prev_difference:
                    result = sumx  
                    prev_difference = difference
                    
                if sumx > target:
                    end -= 1
                elif sumx < target:
                    start += 1
                    
        return result
                

                
                
                
                
                
                
                
        
