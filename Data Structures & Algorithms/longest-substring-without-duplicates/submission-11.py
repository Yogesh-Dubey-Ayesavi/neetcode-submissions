class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        i = 0
        m = set()
        lc = 0

        while i < len(s):
            if s[i] in m:
                # Remove characters until the duplicate is removed
                for k in range(lc, i + 1):
                    m.remove(s[k])

                    if s[k] == s[i]:
                        lc = k + 1
                        break

            m.add(s[i])

            longest = max(longest, i - lc + 1)

            i += 1

        return longest