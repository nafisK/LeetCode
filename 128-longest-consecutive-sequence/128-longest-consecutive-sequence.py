class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
       # Efficient
    
        # turns into set to remove duplicates and for constant lookup (https://stackoverflow.com/a/44080017/12461363)
        nums = set(nums)
        max_length = 0
        
        # iterates through each value in set
        for n in nums:
            
            # if there is no previous value of n, it means its a start
            if n - 1 not in nums:
                
                # using start for code readability
                start = n
                
                # keep checking for next values from start to get upto the last one
                while start in nums:
                    start += 1
                
                # dif between original start and new start which is the end of the seq.
                diff = start - n
                
                # finds max of the prev. consec and the new consec
                max_length = max (max_length, diff)
                
        # returns the max
        return max_length