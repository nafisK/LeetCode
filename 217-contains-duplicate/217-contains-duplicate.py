class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # hashset to store integers
        hashSet = set()
        
        # iterating through all the indexes
        for num in nums:
            
            # checking to see if int already seen before
            if num in hashSet:
                return True
            
            # adding int to set if not seen before
            else:
                hashSet.add(num)
                
        return False