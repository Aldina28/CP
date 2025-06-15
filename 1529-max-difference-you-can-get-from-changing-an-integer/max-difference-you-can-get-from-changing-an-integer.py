class Solution:
    def maxDiff(self, num: int) -> int:
        max_num = str(num)
        max_number = '0'
        min_number = '0'
        for i in str(num):
            if i!='9':
                max_number = i
                break
        max_num = max_num.replace(max_number, '9')
        min_num = str(num)
        for i in str(num):
            if i!='1' and i!='0':
                min_number = i
                break
        num=str(num)
        if num[0]=='1' in num:
            min_num = min_num.replace(min_number, '0')
        else:
            min_num = min_num.replace(min_number, '1')
        print(max_num)
        print(min_num)
        return int(max_num)-int(min_num)


