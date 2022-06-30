

class Solution:
    
    def myAtoi(self, s: str) -> int:
        
        max_INT = 2**31-1
        min_INT = -2**31
        
        res = 0
        i = 0
        degree = 1
        #white space
        while(i < len(s) and s[i] == ' ' ):
            i+=1
            
        if i < len(s) and s[i] == '-':
            degree = -1
            i+=1
        elif i < len(s) and s[i] == '+':
            i+=1
        myset = ('0123456789')
        while(i < len(s) and s[i] in myset):
            res = res*10 + int(s[i])
            i+=1
        res =  res*degree
        if res > 0:
            return min(res,max_INT)
        else:
            return max(res,min_INT)

        
        

            
        
            
        