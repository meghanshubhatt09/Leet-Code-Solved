


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        result = []
        
        
        if len(intervals) == 1:
            return intervals
        
        
        result.append(intervals[0])
        
        for i in range(1,len(intervals)):
            
            if result[-1][1] >= intervals[i][0]:
                x = min(result[-1][0],intervals[i][0])
                y = max(result[-1][1],intervals[i][1])
                
                result[-1][0], result[-1][1] = x,y
            else:
                result.append(intervals[i])
        return result

                
            
            
            
        