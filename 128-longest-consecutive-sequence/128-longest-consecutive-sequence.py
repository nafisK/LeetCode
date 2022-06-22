class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Brute Force
        
        # edge-case
        if not nums:
            return 0
        
        # makes num a set -> turns the set back into a list -> sorts the list -> saves the list
        nums = sorted(list(set(nums)))
        
        # sofar: keeps track of the length, output: 
        sofar, output = 1, 1
        
        # iterate from 2nd element to end
        for i in range(1, len(nums)):
            
            # check prev. element with curr element
            if nums[i - 1] + 1 == nums[i]:
                # increment with consec
                sofar += 1
            else:
                # reset sofar if not consec
                sofar = 1
            
            # after each iteration, find the new max and set to output
            output = max(output ,sofar)
        
        return output