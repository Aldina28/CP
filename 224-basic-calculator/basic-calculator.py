class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        num = 0
        sign = 1
        stack = [sign]
        for numbers in s:
            if numbers.isdigit():
                num = num*10+int(numbers)
            elif numbers == '(':
                stack.append(sign)
            elif numbers ==')':
                stack.pop()
            elif numbers == "+" or numbers=="-":
                result+=sign*num
                sign = (1 if numbers=="+" else -1) * stack[-1]
                num = 0
        return result+sign*num