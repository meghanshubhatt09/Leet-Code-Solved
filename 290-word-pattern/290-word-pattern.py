class Solution:
    
    
    def pattern_dict(self, pattern):
        
        pattern_count = 1
        i = 0
        my_pattern_dict = {}
        
        while(i < len(pattern)):
            if pattern[i] not in my_pattern_dict:
                my_pattern_dict[pattern[i]] = pattern_count
                pattern_count += 1
            i+=1
        return my_pattern_dict
    
    def make_str(self,s,my_dict):
        i = 0
        my_str = ''
        while(i < len(s)):
            my_str += str((my_dict[s[i]]))
            i+=1
            
        return my_str
            
        
    
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        my_pattern_dict = self.pattern_dict(pattern)
        my_s_dict = self.pattern_dict(s.split())
        
        my_pattern_str = self.make_str(pattern, my_pattern_dict)
     
        my_s_str = self.make_str(s.split(), my_s_dict)
        print(my_pattern_str,my_s_str)
        if my_pattern_str == my_s_str:
            return True
        else:
            return False
        
        
        