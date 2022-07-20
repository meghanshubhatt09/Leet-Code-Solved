import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        i = 0
        new_string = re.sub(r'[^\w\s]', ' ', paragraph)
        mylst = new_string.lower().split(' ')
        banned_new = [i.lower() for i in banned]
        word_Set = dict()
        for i in mylst:
            key = i
            if key not in banned_new and len(key)>0:
                if key not in word_Set:
                    word_Set[key] = 1
                else:
                    word_Set[key] += 1
        max_value = 0      
        word = ''
        for key,value in word_Set.items():
            if value > max_value:
                max_value = value
                word = key
        return word
                
                
            

            
        
        