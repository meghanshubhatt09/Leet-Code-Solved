class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i = 0
        j = len(height)-1
        n = len(height)
        res = 0
        
        while(i < j):
            if height[i] <= height[j]:
                curr_res = height[i] * (j-i)
                res = max(res,curr_res)
                i+=1
            else:
                curr_res = height[j] * (j-i)
                res = max(res,curr_res)
                j-=1
        return res
            
            
        