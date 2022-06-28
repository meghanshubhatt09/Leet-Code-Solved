class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        startIndex,endIndex = 0,0
        count = 0
        my_set = set()
        max_result = 0
        
        while(endIndex < len(s)):
            
            if s[endIndex] not in my_set:
                my_set.add(s[endIndex])
                count+=1
                endIndex+=1
                max_result = max(max_result,count)
                
            else:
                my_set.remove(s[startIndex])
                startIndex += 1
                count -= 1
        return max_result

                    
        
        
        
        
        
        
        
        
        
        '''
        a_pointer = 0
        b_pointer = 0
        count = 0
        
        my_set = set()
        
        while(b_pointer < len(s)):
            if s[b_pointer] not in my_set:
                my_set.add(s[b_pointer])
                b_pointer+=1
                count = max(len(my_set),count)
            else:
                my_set.remove(s[a_pointer])
                a_pointer+=1
        return count
        '''

                    
        