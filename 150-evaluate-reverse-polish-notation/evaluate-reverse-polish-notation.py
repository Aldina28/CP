class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for num in tokens:
            if num.isnumeric() or (num[0]=="-" and len(num)>1):
                stack.append(int(num))
            elif len(stack)>=2:
                operand1 = int(stack.pop())
                operand2 = int(stack.pop())
                if num == "+":
                    stack.append(operand1 + operand2)
                elif num == "-":
                    stack.append(operand2 - operand1)
                elif num == "*":
                    stack.append(operand1*operand2)
                elif num=="/":
                    stack.append(int(operand2/operand1))
        return stack[0]