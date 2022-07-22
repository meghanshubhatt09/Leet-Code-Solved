class Solution:
    def minWindow(self, s: str, t: str) -> str:

        end_index = 0
        count = 0
        res = float(inf)
        start_result,end_result = -1,-1
        
        pattern_dict = {}
        window_dict = {}
        
        if len(t)>len(s):
            return ''
        
        if len(t)=='':
            return ''
        
        
        for i in range(len(t)):
            pattern_dict[t[i]] = pattern_dict.get(t[i],0)+1
            
            
        for start_index in range(len(s)):
            start = s[start_index]
            window_dict[start] = window_dict.get(start,0)+1
            
            
            if start in pattern_dict and window_dict[start]==pattern_dict[start]:
                count+=1
           
      
                
            
            while(count == len(pattern_dict)):
                
                if res > start_index-end_index+1:
                    res = start_index-end_index+1
                    start_result, end_result = start_index, end_index
                
                

                end = s[end_index]
                window_dict[end] -= 1
                
                if end in pattern_dict and window_dict[end]<pattern_dict[end]:
                    count-=1
                    
                end_index+=1
                
                
        
        return s[end_result:start_result+1] if res != float(inf) else ''
                
            
                
            
            
            
            
        
 
                
                
                
                
            
            
        
        

        
        

        

        
        
        