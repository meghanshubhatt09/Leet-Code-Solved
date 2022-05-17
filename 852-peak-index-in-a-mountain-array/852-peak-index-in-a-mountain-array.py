class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        
        low = 0
        high = len(arr) - 1
        res = 0
        while(low <= high):
            
            mid = (low+high)//2
            print(low,mid,high)
            if arr[mid] >= arr[mid+1] and arr[mid] >= arr[mid-1]:
                return mid
            elif mid > 0 and arr[mid-1] > arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
                res = low
                
        return res
            
        