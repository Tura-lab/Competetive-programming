class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        
        path = [l for l in path if l]
        
        stack = []
        
        for l in path:
            if l == '..':
                if stack:
                    stack.pop()
            elif l != '.':
                stack.append(l)
                
                
        return '/' + '/'.join(stack)