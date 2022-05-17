class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        ascii_letters = [ord(i) for i in letters]
        ascii_target = ord(target)
        
        low = 0
        high = len(ascii_letters)-1
        res = 0
        while(low<=high):
            mid = (low+high)//2
            
            if ascii_letters[mid] > ascii_target:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return letters[res]
                
        