class Solution:
    def simplifyPath(self, path: str) -> str:
        actual_path = []
        
        for i in path.split('/'):
            if i == '/' or i == '.' or i == '':
                continue
            if actual_path and i == '..':
                actual_path.pop()
            elif i != '..':
                actual_path.append(i)
                
        return '/' + '/'.join(actual_path)