class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        
        for p in S:
            if p == "(":
                stack.append(0)
            else:
                elem = stack.pop()
                stack[-1] +=max(2*elem,1)
                
        return stack.pop()
