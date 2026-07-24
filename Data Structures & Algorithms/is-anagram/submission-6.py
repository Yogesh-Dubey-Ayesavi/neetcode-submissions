class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            seen = set(s)
            for item in seen:
                if item not in t:
                    return False
                sCount = s.count(item)
                tCount = t.count(item)
                if sCount != tCount:
                    return False
            return True
                