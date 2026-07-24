class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join(c.lower() for c in s if c.isalnum())
        print(result,result[0:len(result)],result[::-1])
        return result[0:len(result)]==result[::-1]
        