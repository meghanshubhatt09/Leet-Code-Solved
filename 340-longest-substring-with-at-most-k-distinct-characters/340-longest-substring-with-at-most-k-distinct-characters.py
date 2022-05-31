class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        a_pointer = 0
        b_pointer = 0
        count,result = 0,0
        my_dict = dict()
        
        if k == 0:
            return 0
        
        while (b_pointer < len(s)):
            if s[b_pointer] in my_dict:
                my_dict[s[b_pointer]] += 1
                count += 1
                result = max(count,result)
                b_pointer += 1
            else:
                if (len(my_dict) < k):
                    my_dict[s[b_pointer]] = 1
                    count += 1
                    result = max(count,result)
                    b_pointer += 1
                else:
                    my_dict[s[a_pointer]] -= 1 
                    if my_dict[s[a_pointer]] <= 0:
                        del my_dict[s[a_pointer]]
                    count-=1
                    a_pointer+=1
        return result
            
        