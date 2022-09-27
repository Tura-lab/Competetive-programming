class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        n = len(dominoes)
        rightsToTheLeft = [-1]*n
        leftsToTheRight = [-1]*n
        
        index = -1
        for i in range(n):
            if dominoes[i] == 'R':
                index = i
            elif dominoes[i] == 'L':
                index = -1
            
            rightsToTheLeft[i] = index
            
        index = -1
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'R':
                index = -1
            elif dominoes[i] == 'L':
                index = i
            
            leftsToTheRight[i] = index
        
        for i in range(n):
            if dominoes[i] != '.': continue    
            if leftsToTheRight[i] == rightsToTheLeft[i] == -1:continue
                
            if leftsToTheRight[i] == -1:
                dominoes[i] = 'R'
            elif rightsToTheLeft[i] == -1:
                dominoes[i] = 'L'
            else:
                if leftsToTheRight[i]-i < i-rightsToTheLeft[i]:
                    dominoes[i] = 'L'
                elif leftsToTheRight[i]-i > i-rightsToTheLeft[i]:
                    dominoes[i] = 'R'
        
        return ''.join(dominoes)

            