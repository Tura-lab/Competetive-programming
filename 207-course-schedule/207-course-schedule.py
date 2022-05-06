class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        courses = {}
        seen = set()
        instack = set()
        
        for pre in prerequisites:
            pre.append(-1)
            if pre[0] in courses:
                courses[pre[0]].append(pre[1])
            else:
                courses[pre[0]] = [pre[1]]
            if pre[1] not in courses:
                courses[pre[1]] = []
        
        def dfs(node):
            instack.add(node)
            for n in courses[node]:
                if n in instack:
                    return False
                
                if n not in seen:
                    ans = dfs(n)
                    if ans==False:
                        return ans
            
            instack.remove(node)
            seen.add(node)
            
        for i in range(len(prerequisites)):
            for j in range(2):
                if prerequisites[i][j] not in seen:
                    ans = dfs(prerequisites[i][j])
                    if ans == False:
                        return False
        return True