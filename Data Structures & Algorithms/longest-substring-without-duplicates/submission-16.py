class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     longest = 0
    #     i = 0
    #     m = set()
    #     lc = 0
    #     current = 0
    #     while i < len(s):
    #         if s[i] in m:
    #             for k in range(lc, i + 1):
    #                 m.remove(s[k])
    #                 current -= 1
    #                 if s[k] == s[i]:
    #                     lc = k + 1
    #                     break
    #         m.add(s[i])
    #         i += 1
    #         current += 1
    #         longest = max(current, longest)
    #     return longest

    def lengthOfLongestSubstring(self, s: str) -> int:
            left = 0
            seen = set()
            right = 0
            best=0
            for right in range(len(s)):
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1
                seen.add(s[right])
                best=max(best, right-left+1)
            return best