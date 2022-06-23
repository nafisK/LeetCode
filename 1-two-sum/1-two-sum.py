class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # compliment + nums[i] = target
        # target - nums[i] = compliment
        
        if len(nums) < 2:
            return []
        
        hashmap = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashmap:
                return [hashmap[compliment], i]
            else:
                hashmap[nums[i]] = i;
                
        return []