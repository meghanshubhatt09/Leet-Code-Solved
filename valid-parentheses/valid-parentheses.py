class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        my_stack = []
        myset = {'(','{','['}
        while(i<len(s)):
            
            if s[i] in myset:
                my_stack.append(s[i])
                i+=1
            else:
                if len(my_stack) == 0:
                    return False
                x = my_stack.pop()
                if (s[i] == ')' and x == '(') or (s[i] == '}' and x == '{') or (s[i] == ']' and x == '['):
                    i+=1
                else:
                    return False
        if len(my_stack) != 0:
            return False
            
        return True
        
        
        