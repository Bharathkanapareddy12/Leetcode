class Solution(object):
    def twoSum(self, nums, target):
        num_to_index = {}  
    
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
        
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            num_to_index[num] = i
            
        return []