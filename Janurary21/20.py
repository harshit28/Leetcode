class Solution:
    def isValid(self, s: str) -> bool:
        o_b = {'(':')','{':'}','[':']'}
        stack =[]
        
        for char in s:
            
            if char in o_b:
                stack.append(char)
                
            else:
                if stack and o_b[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
        
