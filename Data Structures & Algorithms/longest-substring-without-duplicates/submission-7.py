class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        for i in range(len(s)):
            k=i
            long=0
            m=set()
            while k < len(s):
                if s[k] in m:   
                    break
                m.add(s[k])
                k+=1
                long+=1
                longest=max(long, longest)
        return longest

            
            
# dvdf