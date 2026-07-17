class Solution:
    def isPalindrome(self, s: str) -> bool:
        prep = [c for c in s.lower() if c.isalnum()]
        return prep == prep[::-1]