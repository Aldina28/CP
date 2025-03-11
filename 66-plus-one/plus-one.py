class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res_str = ""
        for i in range(len(digits)):
            res_str += str(digits[i])
        res_str = int(res_str)
        res_str+=1
        return list(map(int, str(res_str)))