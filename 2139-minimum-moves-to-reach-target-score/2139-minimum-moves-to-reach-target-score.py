class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        steps = 0
        '''
        19, 2
        19//2 = 9
        9 // 4
        '''
        for _ in range(maxDoubles):
            if target == 1:
                break
                
            if target % 2 == 1:
                target -=1
                steps += 1
            target //= 2
            steps += 1
        
        steps += (target - 1)
        return steps