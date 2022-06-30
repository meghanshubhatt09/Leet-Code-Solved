class Solution:
    
    
    def intToRoman(self, num: int) -> str:
        
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbol = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        res = ''
        i = 0
        while(i < len(values) and num != 0):
            if num-values[i] >= 0:
                res = res + symbol[i]
                num = num-values[i]
            else:
                i+=1
        return res
                    
        
        
        
    
           
                
            
            
        

            

            
                    
        
    
        
        
        