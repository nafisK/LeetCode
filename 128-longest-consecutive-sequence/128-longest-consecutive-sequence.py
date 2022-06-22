class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
       # Efficient
        nums = set(nums)
        max_length = 0
        # iterate through nums
        # if you find a start,
            # Keep iterating until you find the last consec num from that start in the set
                # iterate start by one until you hit the end | lets name it end
            # get the diff of end - start
        # check if output of current consec is greater than last consec
        
        for n in nums:
            if n - 1 not in nums:
                start = n
                while start in nums:
                    start += 1
                    
                max_length = max (max_length, start - n)
                
        return max_length