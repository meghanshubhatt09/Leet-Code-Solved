class Solution:
    

    
    
    def letterCombinations(self, digits: str) -> List[str]:
        phone_number = {'2':'abc','3':'def','4':'ghi', '5':'jkl', '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        result = []
        
        
        #### BACKTRACKING
        def createCombinations(i, currString):
            
            if len(currString) == len(digits):
                result.append(currString)
                return 
                
            for char in phone_number[digits[i]]:
                createCombinations(i+1, currString+char)
        
        
        if digits:
            createCombinations(0,'')
        
        return result
        
        

    
      
        