class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Brute Force
        if not nums:
            return 0
        
        nums = sorted(list(set(nums)))
        
        sofar, output = 1, 1
        
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                sofar += 1
            else:
                sofar = 1
            output = max(output ,sofar)
        
        return output