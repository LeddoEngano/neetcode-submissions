class Solution:
    def isValid(self, s: str) -> bool:
        # ({[()]})
        pairs = { 
            '}':'{',
            ')':'(',
            ']':'['
        }
        stack = []

        if len(s) <= 1:
            return False  

        for c in s:
            if c in pairs: # closing )      {[( )]}  stack=[ '{', '[', '(' ]
                if stack and pairs[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else: # opening
                stack.append(c)

        return True if not stack else False