class Solution:
    def isValid(self, s: str) -> bool:
        closing_conds = {")": "(", "}": "{", "]":"["}
        # For stack imp., use deque
        stack = deque()
        for c in s:
            if c in closing_conds:
                if closing_conds[c] and len(stack) > 0 and stack[-1] == closing_conds[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
            
