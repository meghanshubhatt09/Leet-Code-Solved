class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        
        a = max(arr)
        my_arr = [0]*((a+k)+1)
        
        for i in range(len(arr)):
            my_arr[arr[i]] += 1
            
        my_arr[:] = my_arr[1:]
        
        print(my_arr)
        
        if 0 not in my_arr:
            return len(my_arr) + k
        
        count = 0
        for i in range(len(my_arr)):
            if count == k:
                return i
            if my_arr[i] == 0:
                count += 1
        return i+1
                
            
        
        
            
        
            
            
        