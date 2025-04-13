class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] == "-":
            res_x = str(x)[len(str(x)):0:-1]
            res_x = int("-" + res_x)     
        else:
            res_x = str(x)[::-1]
            res_x = int(res_x) 
        if res_x in range(-2**31, 2**31):
            return res_x
        else:
            return 0