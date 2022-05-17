class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        votes = 0
        for i in range(len(nums)):
            
            if votes == 0:
                candidate = nums[i]
                votes += 1
            else:
                if candidate == nums[i]:
                    votes += 1
                else:
                    votes -=1
            print(candidate,votes)
        
        count = 0
        for j in range(len(nums)):
            if candidate == nums[j]:
                count += 1
        
        print(count,candidate)
        if count > len(nums)//2:
            return candidate
        else:
            return 'There is no majority element'
            
            
        