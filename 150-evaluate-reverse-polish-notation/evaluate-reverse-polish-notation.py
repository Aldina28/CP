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
        stk = []
        for i in tokens:
            if i not in ["+", "-", "/", "*"]:
                stk.append(i)
            else:
                a = int(stk.pop())
                b = int(stk.pop())
                print(a,b)
                if i=="+":
                    res = a+b
                elif i=="-":
                    res = b-a
                elif i=="*":
                    res = a*b
                elif i=="/":
                    if b < 0 and a < 0:
                        res = b//a
                    elif b < 0 or a < 0:
                        res = abs(b)//abs(a) * -1
                    else:
                        res = b//a

                stk.append(res)

        return int(stk.pop())