class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n//2
        
        left = num[:mid]
        right = num[mid:]
        
        left_count = right_count = 0
        left_sum = right_sum = 0
        
        for l in left:
            if l!='?':
                left_sum += int(l)
            left_count  += l=='?'

        for l in right:
            if l!='?':
                right_sum += int(l)
            right_count += l=='?'
        
        if (left_count + right_count) & 1:
            return True
        if left_count == right_count:
            return left_sum != right_sum
        
        

        if right_sum > left_sum:
            if ((left_count - right_count)//2)*9 == right_sum-left_sum:
                return False
        elif left_sum > right_sum:
            if ((right_count - left_count)//2)*9 == left_sum-right_sum:
                return False
        
        return True