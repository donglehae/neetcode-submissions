class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for c in s:
            if stack and c in pairs:
                if stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        
        return False if stack else True