class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key = lambda x:len(x))
        def ok(path):
            i=len(path)-1
            if path in seen:
                return False
            
            while i>=0:
                if path[i]=='/' and path[:i] in seen:
                    return False
                i-=1
            return True
        
        seen = set()
        for path in folder:
            if ok(path):
                seen.add(path)
        
        return list(seen)
            # '''    "/a/ca","/a/b/ca","/a/b/de","/a","/a/b","/d","/c/d/af","/c/f","/a/d/cd","/a/b/ds","/as/h","/a/b/ga","/a/f/de","/ao","/a/b/t","/e","/c/d/ef","/c/t","/e/b/cd","/a/t/ds"
            # '''