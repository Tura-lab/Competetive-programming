class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        path = []
        if not prerequisites:
            for i in range(numCourses):
                path.append(i)
            return path
        courses = {}
        for pre in prerequisites:
            if pre[0] not in courses:
                courses[pre[0]] = [pre[1]]
            else:
                courses[pre[0]].append(pre[1])
            if pre[1] not in courses:
                courses[pre[1]] = []
        
        instack = set()
        seen = set()
        
        
        # print(courses)
        def dfs(node):
            instack.add(node)
            for n in courses[node]:
                if n in instack:
                    return []
                if n not in seen:
                    ans = dfs(n)
                    # print(path)
                    if ans == []:
                        return [] 
            instack.remove(node)
            # print(node)
            if node not in seen:
                seen.add(node)
                path.append(node)
                
            
        for i in range(len(prerequisites)):
            for j in range(2):
                if dfs(prerequisites[i][j]) == []:
                    return []
        for i in range(numCourses):
            if i not in seen:
                path.append(i)
        
        return path
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        