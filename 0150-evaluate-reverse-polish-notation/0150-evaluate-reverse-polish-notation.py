class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                # Pop the top two numbers from the stack
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # Division
                    # Python division needs truncation toward zero
                    stack.append(int(a / b))
            else:
                # Token is a number, push to stack
                stack.append(int(token))
        
        # The final result is the only element in the stack
        return stack[0]
