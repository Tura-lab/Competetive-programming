class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        
        vals = sorted(symbols.keys(), reverse = True)

        ans = []
        cur, i = 0, 0
        while cur < num:
            while vals[i] + cur <= num:
                cur += vals[i]
                ans.append(symbols[vals[i]])
            i += 1
        
        return "".join(ans)