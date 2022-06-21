class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1
            
        divisor = len(str1)
        while divisor>0:
            if len(str1)%divisor != 0 or len(str2)%divisor != 0:
                divisor -=1
                continue
            
            if str1[:divisor]*(len(str2)//divisor) == str2 and str1[:divisor]*(len(str1)//divisor) == str1:
                return str1[:divisor]
            divisor-=1
        return ""
            
            