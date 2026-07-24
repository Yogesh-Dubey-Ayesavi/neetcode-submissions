from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            i = num
            length = 0
            while i in s:
                length += 1
                i += 1
            longest = max(longest, length)

        return longest