class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
                    
        def dfs(city):
            seen.add(city)
            for i, j in enumerate(isConnected[city]):
                if i not in seen and j==1:
                    dfs(i)
                    
        provinces = 0
        for i in range(len(isConnected)):
            if i not in seen:
                dfs(i)
                provinces +=1
                
        return provinces
        
        
        