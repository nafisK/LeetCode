class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Use a hashmap to communite between both s and t
        # increment count for each char when s
        # decrement count for each char when t
        # if all chars.keys dont have 0, return false
        # else true
        
        if len(s) != len(t):
            return False
        
        arr = [0 for i in range(26)]
        
        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] += 1
            arr[ord(t[i]) - ord('a')] -= 1
            
        for i in arr:
            if i != 0:
                return False
            
        return True
                