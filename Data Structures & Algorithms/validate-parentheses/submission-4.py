class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapped = {')': '(', '}': '{', ']': '['}

        for c in s:
            if stack and c in mapped:
                if stack.pop() != mapped[c]:
                    return False
            else:
                stack.append(c)
        
        return False if stack else True