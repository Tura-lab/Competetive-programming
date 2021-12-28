class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num_arr = []
        for i in range(len(num)):
            while len(num_arr) > 0 and k>0 and int(num[i]) < int(num_arr[-1]):
                k-=1
                num_arr.pop()
            num_arr.append(num[i])
        while k>0:
            k-=1
            num_arr.pop()
        return "0" if num_arr==[] else str(int(''.join(num_arr)))
