class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = []
        num = 0
        prev_op = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            # If it's an operator or we are at the last char
            if char in '+-*/' or i == len(s) - 1:
                if prev_op == '+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack[-1] = stack[-1] * num
                elif prev_op == '/':
                    stack[-1] = int(stack[-1] / num)  # Truncate toward zero
                prev_op = char
                num = 0

        return sum(stack)