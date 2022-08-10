class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        time_start = []
        time_end = []
        for time in range(len(intervals)):
            time_start.append(intervals[time][0])
            time_end.append(intervals[time][1])
        time_start.sort()
        time_end.sort()
        
        i = 0
        j = 0
        meetingRooms = 0
        count = 0
        while(i < len(time_start) and j < len(time_end)):
            if time_start[i] < time_end[j]:
                count += 1
                meetingRooms = max(meetingRooms, count)
                i+=1
            else:
                count -= 1
                j+=1
                
        return meetingRooms