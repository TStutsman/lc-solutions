class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # iterate over tokens
        # if integer, store in operand
        # if operator, operate
        stack = []

        for token in tokens:
            if token == '+':
                top = stack.pop()
                stack[-1] += top

            elif token == '-':
                top = stack.pop()
                stack[-1] -= top

            elif token == '/':
                top = stack.pop()

                if stack[-1] * top < 0:
                    stack[-1] //= -top
                    stack[-1] *= -1
                else:
                    stack[-1] //= top

            elif token == '*':
                top = stack.pop()
                stack[-1] *= top

            else:
                stack.append(int(token))
        
        return stack[-1]