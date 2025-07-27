class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        ones = {
            1:"One", 
            2:"Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }

        teens = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }
        tens = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }
        endings = ["", " Thousand", " Million" , " Billion"]
        def group(val):
            #314, 304, 340, 300, 004
            arr = []
            hundreds = val // 100
            if hundreds:
                arr.append(ones[hundreds] + " Hundred")
            last2 = val % 100
            if last2:
                if last2 < 10:
                    arr.append(ones[last2])
                elif last2 < 20:
                    arr.append(teens[last2])
                else:
                    tens_part, ones_part = last2//10, last2%10
                    arr.append(tens[10 * tens_part])
                    if ones_part:
                        arr.append(ones[ones_part])
            return " ".join(arr)
        i = 0
        res = []
        while num:
            val = group(num % 1000)
            if val:
                res.append(val + endings[i])
            i += 1
            num //= 1000
        res.reverse()
        return " ".join(res)