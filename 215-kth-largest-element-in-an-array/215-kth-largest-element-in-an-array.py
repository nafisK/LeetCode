class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Brute Force
        nums = sorted(nums)
        return nums[0 - k]