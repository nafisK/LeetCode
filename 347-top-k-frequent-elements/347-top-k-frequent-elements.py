class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        # add count to dictionary
        for n in nums:
            
            # get count and increment it or set it to 0
            count[n] = 1 + count.get(n, 0)
            
        # sets value to the count index
        # count => {1: 3, 2: 2, 3: 1}
        # freq => [[], [3], [2], [1], [], [], []]
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        # iterate freq time from index 0 to negative direction
        for i in range(len(freq) - 1, 0, -1):
            
            # accounts for multiple values in index
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
            