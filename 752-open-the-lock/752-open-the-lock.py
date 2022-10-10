class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        q = deque(['0000'])
        visited = set(['0000'])
        
        level = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node == target:
                    return level
                if node in deadends:
                    continue
                
                for i in range(4):
                    if node[i] == '0':
                        new1 = node[:i] + '1' + node[i+1:]
                        new2 = node[:i] + '9' + node[i+1:]
                    elif node[i] == '9':
                        new1 = node[:i] + '0' + node[i+1:]
                        new2 = node[:i] + '8' + node[i+1:]
                    else:
                        new1 = node[:i] + str(int(node[i])+1) + node[i+1:]
                        new2 = node[:i] + str(int(node[i])-1) + node[i+1:]
                        
                    if new1 not in visited:
                        visited.add(new1)
                        q.append(new1)
                    if new2 not in visited:
                        visited.add(new2)
                        q.append(new2)
                        
            level += 1
            
        return -1
                        
                        
            
                
                