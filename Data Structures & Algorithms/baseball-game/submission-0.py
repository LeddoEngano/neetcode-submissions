class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # We'll use a stack
        # C -> pop()
        # D appends 2 * [-1]
        # + -> appends [-1] + [-2]

        # summ of all items from the stack

        summ = 0
        stack = []

        for op in operations:
            if op == "C":
                stack.pop()
                continue
            if op == "D":
                mult = 2 * int(stack[-1])
                stack.append(mult)
                continue
            if op == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
                continue
            else:
                stack.append(op)
        
        for i in stack:
            summ += int(i)

        return summ