class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = list()
        
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                # if current number and the previous is same then we will yeild same result set
                # no skip it
                continue
            start = i+1
            end = len(nums)-1
            
            while(start < end):
                   
                ans = nums[i] + nums[start] + nums[end]
                
                if ans == 0:
                    
                    x = [nums[i],nums[start],nums[end]]
                    #if x not in result:
                    result.append(x)
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1 
                        # here for a current number in index i
                        # if current start and previous start is same then we will yeild same result 
                        #set
                    
                    
                if ans > 0:
                    end -= 1
                if ans < 0 :
                    start += 1
        return result
                    
                    