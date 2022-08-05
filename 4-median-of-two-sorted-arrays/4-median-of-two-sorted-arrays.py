class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        first_index = 0
        second_index = 0
        result = []
        while(first_index<len(nums1) and second_index<len(nums2)):
            if nums1[first_index] > nums2[second_index]:
                result.append(nums2[second_index])
                second_index += 1
            elif nums1[first_index] < nums2[second_index]:
                result.append(nums1[first_index])
                first_index += 1
            else:
                result.append(nums1[first_index])
                first_index += 1
                
        
        if first_index < len(nums1):
            for i in range(first_index,len(nums1)):
                result.append(nums1[i])
            
        if second_index < len(nums2):
            for i in range(second_index,len(nums2)):
                result.append(nums2[i])
        n = len(result)     
        return (result[n//2-1]/2.0+result[n//2]/2.0, result[n//2])[n % 2] if n else None
                
  
        