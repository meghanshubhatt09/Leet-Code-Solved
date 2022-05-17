class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        low,high = 0,len(nums)-1
        
        if len(nums) == 1 and nums[0] == target:
            return low
        if len(nums) == 1 and nums[0] != target:
            return -1
        
        while (low <= high):
        
            mid = (high+low)//2
            print(low,mid,high)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        