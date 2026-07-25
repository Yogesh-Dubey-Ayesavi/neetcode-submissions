class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        maxFreq = 0
        longest = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            # Highest frequency character in the current window
            maxFreq = max(maxFreq, count[s[right]])

            # If more than k replacements are needed,
            # shrink the window
            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1

            # Window is valid
            longest = max(longest, right - left + 1)

        return longest