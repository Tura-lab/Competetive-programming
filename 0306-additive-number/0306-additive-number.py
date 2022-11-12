class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        if len(num) < 3:
            return False
        
        def check(first, second, i):
            j = i
            
            while j < len(num):
                if num[i] == '0' and num[j] == '0' and j-i+1 > 1:
                    j+=1
                    continue
                if num[i] == '0' and num[j] != '0':
                    j+=1
                    continue
                if int(num[i:j+1]) == first + second:
                    first = second
                    second = int(num[i:j+1])
                    i = j+1
                j+=1

            return i == j
        
        for i in range(len(num)-1):
            if num[0] == '0' and num[i] == '0' and i-0+1 > 1:
                continue
            if num[0] == '0' and num[i] != '0':
                continue
                
            for j in range(i+1, len(num)-1):
                if num[i+1] == '0' and num[j] == '0' and j-i+1-1 > 1:
                    continue
                if num[i+1] == '0' and num[j] != '0':
                    continue
                    
                if check(int(num[:i+1]), int(num[i+1:j+1]), j+1):
                    return True
                
        return False