class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack = []
        # for num in tokens:
        #     if num.isnumeric() or (num[0]=="-" and len(num)>1):
        #         stack.append(int(num))
        #     else:
        #         operand1 = stack.pop()
        #         operand2 = stack.pop()
        #         if num == "+":
        #             stack.append(operand1 + operand2)
        #         elif num == "-":
        #             stack.append(operand2 - operand1)
        #         elif num == "*":
        #             stack.append(operand1*operand2)
        #         elif num=="/":
        #             stack.append(int(operand2/operand1))
        # return stack[0]
        stack = []
        for token in tokens:
            if token.isdigit() or (token[0] == '-' and len(token) > 1):
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))
        return stack[0]
