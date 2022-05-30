class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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


                    
        