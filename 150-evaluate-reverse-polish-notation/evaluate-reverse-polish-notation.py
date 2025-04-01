class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for num in tokens:
            if num == "+" or num=="-" or num=="*"or num=="/":
                if len(stack)>=2:
                    operand1 = int(stack.pop())
                    operand2 = int(stack.pop())
                    if num == "+":
                        result = operand1 + operand2
                    elif num == "-":
                        result = operand2 - operand1
                    elif num == "*":
                        result = operand1*operand2
                    elif num=="/":
                        result = int(operand2/operand1)
                    stack.append(str(result))
            else:
                stack.append(num)
        return int(stack[0])