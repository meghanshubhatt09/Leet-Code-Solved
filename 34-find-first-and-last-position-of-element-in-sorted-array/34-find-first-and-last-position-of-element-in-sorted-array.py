class Solution:
    
    def firstOcc(self,nums,target):
        low = 0
        high = len(nums)-1
        
        while(low<=high):
            mid = (low+high)//2
            
            if nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid + 1
            else:
                if mid == 0 or nums[mid-1] != target:
                    return mid
                else:
                    high = mid - 1
        return -1
        
        
    def lastOcc(self,nums,target):
        low = 0
        high = len(nums)-1        
        n = high
        
        while(low<=high):
            mid = (low+high)//2

            if nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid + 1
            else:
                if mid == n or nums[mid+1] != target:
                    return mid
                else:
                    low = mid + 1
        return -1
        
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        return [self.firstOcc(nums,target),self.lastOcc(nums,target)]
        

        

        
        