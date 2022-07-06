class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_1 = nums.copy()
        num_2 = nums.copy()
        solution = []
        for i in range(1,len(nums)):
            num_1[i] = num_1[i]*num_1[i-1]

        for i in range(len(nums)-2,-1,-1):
            num_2[i] = num_2[i]*num_2[i+1]
            
        for i in range(len(nums)):
            if nums[i] != 0:
                x = (num_1[i]//nums[i]) * (num_2[i]//nums[i])
            else:
                if i == 0:
                    x = num_2[i+1]
                elif i == len(nums)-1:
                    x =num_1[i-1]
                else:
                    x = num_1[i-1]*num_2[i+1]
            solution.append(x)
        return solution
            
            