class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        # store all values into the hashmap
        # using key: index, value: ints
        for i in range(len(nums)):
            hashmap[nums[i]] = i
            
        # check if compliment if present, if so, return compliment
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
            
            
            
        