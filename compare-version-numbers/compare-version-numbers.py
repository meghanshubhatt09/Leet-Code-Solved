class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        num1 = version1.split('.')
        num2 = version2.split('.')
        score = 0
        i = 0
        j = 0
        while((i < len(num1) or j < len(num2)) and score==0):
            
            if i >= len(num1) and score == 0:
                for n2 in range(j,len(num2)):
                    if int(num2[n2])>0:
                        return -1
                return score
            
            elif j >= len(num2) and score == 0:
                for n1 in range(i,len(num1)):
                    if int(num1[n1])>0:
                        return 1
                return score
            else:
                if int(num1[i]) > int(num2[i]):
                    score += 1
                elif int(num1[i]) < int(num2[i]):
                    score -= 1
                i+=1
                j+=1
        return score
        

                
    